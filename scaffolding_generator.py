from pathlib import Path

# Define the folder structure
base_dir = Path("research-analysis-suite")

folders = [
    "data/raw",
    "data/processed",
    "data/exports",
    "notebooks/interviews",
    "notebooks/surveys",
    "research_methods/interviews",
    "research_methods/surveys",
    "utils",
    "outputs/summaries",
    "outputs/charts",
    "tests",
    "scripts",
]

files = {
    "README.md": """# Research Analysis Suite\n\nA modern research toolkit powered by AI,
    LLMs, statistical models, and smart automation.""",
    ".env": "# Add environment variables like API keys here",
    "pyproject.toml": """
[tool.poetry]
name = "research-analysis-suite"
version = "0.1.0"
description = "A modern research toolkit powered by AI, LLMs,
and statistical analysis."
authors = ["Your Name <you@example.com>"]
readme = "README.md"

[tool.poetry.dependencies]
python = "^3.10"
openai = "*"
pandas = "*"
scikit-learn = "*"
jupyter = "*"
whisper = "*"
numpy = "*"
matplotlib = "*"
transformers = "*"

[build-system]
requires = ["poetry-core"]
build-backend = "poetry.core.masonry.api"
""",
    "utils/__init__.py": "",
    "utils/io.py": "# Helper functions for reading/writing data",
    "utils/llm_tools.py": "# OpenAI GPT, Whisper, etc. wrappers",
    "utils/translation.py": "# Translation helpers",
    "utils/visualization.py": "# Plotting functions",
    "research_methods/__init__.py": "",
    "research_methods/interviews/__init__.py": "",
    "research_methods/interviews/ingestion.py": "# Functions for loading interview data",
    "research_methods/interviews/transcription.py": "# Transcription logic",
    "research_methods/interviews/translation.py": "# Translate transcripts",
    "research_methods/interviews/descriptive.py": "# Basic stats & summaries",
    "research_methods/interviews/exploratory.py": "# Exploratory analysis for interviews",
    "research_methods/surveys/__init__.py": "",
    "research_methods/surveys/ingestion.py": "# Functions for loading survey data",
    "research_methods/surveys/cleaning.py": "# Cleaning survey responses",
    "research_methods/surveys/descriptive.py": "# Descriptive stats for surveys",
    "research_methods/surveys/statistical.py": "# Statistical analysis tools",
    "scripts/run_interviews_pipeline.py": "# Entry point for full interviews pipeline",
    "scripts/run_surveys_pipeline.py": "# Entry point for full surveys pipeline",
    "tests/test_interviews.py": "# Tests for interviews module",
    "tests/test_surveys.py": "# Tests for surveys module",
}

# Create folders
for folder in folders:
    Path(base_dir / folder).mkdir(parents=True, exist_ok=True)

# Create files
for file_path, content in files.items():
    file = base_dir / file_path
    file.parent.mkdir(parents=True, exist_ok=True)
    file.write_text(content.strip())

"Project scaffolding generated successfully."
