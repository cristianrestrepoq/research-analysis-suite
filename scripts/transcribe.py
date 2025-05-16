from pathlib import Path
from research_methods.transcription.whisper import WhisperTranscriber
from utils.file_manager import get_transcription_output_path
from utils.audio_utils import process_audio


def should_skip(audio_path: Path, output_dir: Path) -> bool:
    """Check if a transcription already exists"""
    base_name = audio_path.stem.replace("_compressed", "")
    expected_output = output_dir / f"{base_name}_transcription.txt"
    print(f"Checking if exists: {expected_output}")
    return expected_output.exists()


def main() -> None:
    """Main function to handle audio transcription process."""
    audio_dir = Path("data/raw/interviews")
    print(f"Transcribing audio files in {audio_dir}...")
    output_dir = get_transcription_output_path()
    print(f"Transcriptions will be saved in {output_dir}...")
    transcriber = WhisperTranscriber(output_dir)

    for ext in (
        "*.mp3",
        "*.m4a",
        "*.mp4",
        "*.mpeg",
        "*.mpga",
        "*.wav",
        "*.webm",
        "*.ogg",
    ):
        for audio_path in audio_dir.glob(ext):
            if should_skip(audio_path, output_dir):
                print(f"Skipping {audio_path.name} (already transcribed).")
                continue

            process_single_file(audio_path, output_dir, transcriber)


def process_single_file(
    audio_path: Path, output_dir: Path, transcriber: WhisperTranscriber
) -> None:
    """Process a single audio file for transcription."""
    chunks = process_audio(audio_path)
    full_text = ""

    try:
        for i, chunk in enumerate(chunks):
            print(f"Transcribing chunk {i+1}/{len(chunks)} of {audio_path.name}...")
            try:
                text = transcriber.transcribe(chunk)
                full_text += text + "\n"
            except Exception as e:
                print(f"❌ Failed to transcribe chunk {i+1}: {e}")
                raise

        output_path = output_dir / f"{audio_path.stem}_transcription.txt"
        output_path.write_text(full_text.strip(), encoding="utf-8")
        print(f"✅ Transcribed: {audio_path.name}")

    finally:
        cleanup_temporary_files(audio_path)


def cleanup_temporary_files(audio_path: Path) -> None:
    """Clean up temporary files created during processing."""
    chunks_dir = audio_path.parent / f"{audio_path.stem}_chunks"
    if chunks_dir.exists():
        for chunk in chunks_dir.glob("*.mp3"):
            chunk.unlink()
        chunks_dir.rmdir()

    compressed_path = audio_path.parent / f"{audio_path.stem}_compressed.mp3"
    if compressed_path.exists():
        compressed_path.unlink()


if __name__ == "__main__":
    main()
