from abc import ABC, abstractmethod
from pathlib import Path


class TranscriptionEngine(ABC):
    @abstractmethod
    def transcribe(self, audio_path: Path) -> str:
        pass
