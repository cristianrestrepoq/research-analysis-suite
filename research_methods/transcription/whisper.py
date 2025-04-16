from openai import OpenAI
from pathlib import Path
from .base import TranscriptionEngine
from utils.config import OPENAI_API_KEY, OPENAI_TRANSCRIBE_MODEL

MAX_FILE_SIZE_MB = 15  # Maximum file size for OpenAI API (25 MB)


class WhisperTranscriber(TranscriptionEngine):
    def __init__(self, output_dir: Path):
        self.client = OpenAI(api_key=OPENAI_API_KEY)
        self.model = OPENAI_TRANSCRIBE_MODEL
        self.output_dir = output_dir

    def transcribe(self, audio_path: Path) -> str:
        # Use compressed file if it exists
        compressed_path = audio_path.with_name(
            f"{audio_path.stem}_compressed{audio_path.suffix}"
        )
        if compressed_path.exists():
            audio_to_use = compressed_path
        else:
            audio_to_use = audio_path

        with open(audio_to_use, "rb") as audio_file:
            transcription = self.client.audio.transcriptions.create(
                model=self.model, file=audio_file
            )

        transcription_text = transcription.text
        self._save_transcription(audio_path, transcription_text)
        return transcription_text

    def _save_transcription(self, audio_path: Path, text: str) -> None:
        output_path = self.output_dir / f"{audio_path.stem}_transcription.txt"
        output_path.parent.mkdir(parents=True, exist_ok=True)
        output_path.write_text(text, encoding="utf-8")
