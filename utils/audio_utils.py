from pathlib import Path
import subprocess

MAX_FILE_SIZE_MB = 15


def compress_audio(audio_path: Path) -> Path:
    file_size_mb = audio_path.stat().st_size / (1024 * 1024)
    if file_size_mb <= MAX_FILE_SIZE_MB:
        return audio_path  # No need to compress

    compressed_path = audio_path.with_name(
        f"{audio_path.stem}_compressed{audio_path.suffix}"
    )

    if compressed_path.exists():
        return compressed_path  # Already compressed

    print(f"Compressing {audio_path.name} to reduce file size...")

    try:
        subprocess.run(
            ["ffmpeg", "-i", str(audio_path), "-b:a", "128k", str(compressed_path)],
            check=True,
        )
    except subprocess.CalledProcessError as e:
        print(f"Compression failed: {e}")
        return audio_path

    return compressed_path if compressed_path.exists() else audio_path
