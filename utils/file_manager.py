from pathlib import Path


def get_transcription_output_path(base_dir: str = "outputs/transcriptions") -> Path:
    path = Path(base_dir)
    path.mkdir(parents=True, exist_ok=True)
    return path
