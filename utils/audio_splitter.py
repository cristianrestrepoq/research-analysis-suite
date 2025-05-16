from pathlib import Path
import subprocess

MAX_CHUNK_LENGTH_MS = 10 * 60 * 1000  # 10 minutes
MAX_DURATION_SECONDS = 600  # 10 minutes limit for Whisper


def split_audio(audio_path: Path) -> list[Path]:
    """Split audio into chunks using ffmpeg"""
    output_dir = audio_path.parent / f"{audio_path.stem}_chunks"
    output_dir.mkdir(parents=True, exist_ok=True)

    # Split into 10-minute segments, always output as MP3
    cmd = [
        "ffmpeg",
        "-i",
        str(audio_path),
        "-f",
        "segment",
        "-segment_time",
        str(MAX_DURATION_SECONDS),
        "-c:a",
        "libmp3lame",  # Use MP3 codec
        "-b:a",
        "64k",  # Same bitrate as compression
        "-ar",
        "44100",  # Same audio settings
        "-ac",
        "2",
        str(output_dir / f"{audio_path.stem}_part_%03d.mp3"),
    ]

    subprocess.run(cmd, check=True)

    # Return list of chunk paths in order
    return sorted(output_dir.glob(f"{audio_path.stem}_part_*.mp3"))
