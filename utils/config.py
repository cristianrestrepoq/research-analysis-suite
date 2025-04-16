import os
from dotenv import load_dotenv

load_dotenv()  # Loads the .env file

OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
OPENAI_TRANSCRIBE_MODEL = os.getenv("OPENAI_TRANSCRIBE_MODEL")

if not OPENAI_API_KEY:
    raise EnvironmentError("Missing OPENAI_API_KEY in environment.")
