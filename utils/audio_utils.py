import subprocess
from pathlib import Path
from utils.audio_splitter import split_audio

MAX_FILE_SIZE_MB = 15  # OpenAI API limit
MAX_DURATION_SECONDS = 600  # 10 minutes limit for Whisper


def get_audio_duration(audio_path: Path) -> float:
    """Get duration in seconds using ffprobe"""
    cmd = [
        "ffprobe",
        "-i",
        str(audio_path),  # Added -i flag
        "-v",
        "error",
        "-show_entries",
        "format=duration",
        "-of",
        "default=noprint_wrappers=1:nokey=1",
    ]
    try:
        output = subprocess.check_output(cmd, stderr=subprocess.PIPE).decode().strip()
        return float(output)
    except subprocess.CalledProcessError as e:
        print(f"Error getting duration: {e.stderr.decode()}")
        raise


def compress_audio(audio_path: Path) -> Path:
    """Compress audio file if needed using ffmpeg and convert to MP3"""
    file_size_mb = audio_path.stat().st_size / (1024 * 1024)

    if file_size_mb <= MAX_FILE_SIZE_MB:
        # Convert to MP3 even if size is ok to ensure format consistency
        output_path = audio_path.parent / f"{audio_path.stem}.mp3"
        if output_path.exists():
            return output_path
    else:
        output_path = audio_path.parent / f"{audio_path.stem}_compressed.mp3"
        if output_path.exists():
            return output_path

    cmd = [
        "ffmpeg",
        "-i",
        str(audio_path),
        "-c:a",
        "libmp3lame",
        "-b:a",
        "64k",
        "-ar",
        "44100",  # Sample rate
        "-ac",
        "2",  # Stereo
        "-y",  # Overwrite if exists
        str(output_path),
    ]

    try:
        subprocess.run(cmd, check=True, capture_output=True, text=True)
        return output_path
    except subprocess.CalledProcessError as e:
        print(f"FFmpeg error: {e.stderr}")
        raise


def process_audio(audio_path: Path) -> list[Path]:
    """Process audio file: compress and/or split if needed"""
    try:
        # First convert/compress to MP3
        compressed_path = compress_audio(audio_path)

        # Check duration
        duration = get_audio_duration(compressed_path)

        if duration <= MAX_DURATION_SECONDS:
            return [compressed_path]

        # Split into chunks if too long
        return split_audio(compressed_path)
    except Exception as e:
        print(f"Error processing audio {audio_path}: {str(e)}")
        raise
