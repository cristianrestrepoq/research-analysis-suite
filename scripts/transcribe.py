from pathlib import Path
from research_methods.transcription.whisper import WhisperTranscriber
from utils.file_manager import get_transcription_output_path
from utils.audio_utils import compress_audio

# MAX_SIZE_MB = 15  # Maximum file size for OpenAI API (15 MB)


def should_skip(audio_path: Path, output_dir: Path) -> bool:
    expected_output = output_dir / f"{audio_path.stem}_transcription.txt"
    return expected_output.exists()


# def file_is_too_large(file_path: Path, max_mb: int = MAX_SIZE_MB) -> bool:
#     return file_path.stat().st_size > max_mb * 1024 * 1024


def main():
    audio_dir = Path("data/raw/interviews")
    print(f"Transcribing audio files in {audio_dir}...")
    output_dir = get_transcription_output_path()
    print(f"Transcriptions will be saved in {output_dir}...")
    transcriber = WhisperTranscriber(output_dir)

    for ext in ("*.mp3", "*.m4a", ".mp4", "mpeg", "mpga", "wav", "webm"):
        for audio_path in audio_dir.glob(ext):
            if should_skip(audio_path, output_dir):
                print(f"Skipping {audio_path.name} (already transcribed).")
                continue

            audio_path = compress_audio(audio_path)

            print(f"Transcribing {audio_path.name}...")
            try:
                text = transcriber.transcribe(audio_path)
                print(f"Transcription: {text[:50]}...")  # Print first 50 characters
                print(f"✅ Transcribed: {audio_path.name}")
            except Exception as e:
                print(f"❌ Failed to transcribe {audio_path.name}: {e}")


if __name__ == "__main__":
    main()
