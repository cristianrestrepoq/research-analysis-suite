# Research Analysis Suite

A modern research toolkit powered by AI, LLMs, statistical models, and smart automation to enhance qualitative and quantitative analysis.

## Overview

This toolkit provides functionality for processing and analyzing research data, with a focus on:

- Audio transcription using OpenAI Whisper
- Interview analysis
- Survey processing
- Statistical analysis
- Automated reporting

## Features

### Core Features (Open Source)
- **Audio Processing**
  - Automatic compression and format standardization
  - Smart chunking for large files
  - Support for multiple audio formats
  - Integration with OpenAI Whisper API

### Premium Features (Private)
- **Advanced Analysis Tools**
  - Interview transcription and analysis
  - Survey data processing
  - Statistical analysis
  - Visualization tools
  - LLM-powered insights

## Installation

1. Clone the repository:
```bash
git clone <repository-url>
cd research-analysis-suite
```

2. Install Poetry (if not already installed):
```bash
curl -sSL https://install.python-poetry.org | python3 -
```

3. Install dependencies:
```bash
poetry install
```

4. Set up environment variables:
Create a `.env` file with:
```
OPENAI_API_KEY=your_api_key_here
OPENAI_TRANSCRIBE_MODEL=whisper-1
```

## Prerequisites

- Python 3.10 or higher
- FFmpeg installed on your system (for Windows, download from [ffmpeg.org](https://ffmpeg.org/download.html))
- OpenAI API key

## Usage

### Audio Transcription

Process audio files for transcription:

```bash
poetry run python scripts/transcribe.py
```

Audio files should be placed in `data/raw/interviews/`. Supported formats:
- MP3
- M4A
- MP4
- WAV
- WEBM
- OGG

Transcriptions will be saved in `outputs/transcriptions/`.

### Directory Structure

```
research-analysis-suite/
├── data/
│   ├── raw/          # Raw data files
│   ├── processed/    # Processed data
│   └── exports/      # Final exports
├── notebooks/        # Analysis notebooks
├── outputs/          # Generated outputs
│   ├── transcriptions/
│   ├── summaries/
│   └── charts/
├── research_methods/ # Core analysis modules
└── utils/           # Utility functions
```

## Configuration

Key configuration options in `utils/audio_utils.py`:

- `MAX_FILE_SIZE_MB`: Maximum file size for API uploads (default: 15MB)
- `MAX_DURATION_SECONDS`: Maximum audio duration (default: 600s)

## Development

1. Install development dependencies:
```bash
poetry install --with dev
```

2. Set up pre-commit hooks:
```bash
pre-commit install
```

## Contributing

This project follows a hybrid licensing model:

### Core Features
The core utilities are open source under the MIT License. Contributions are welcome!

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Run tests and linting
5. Submit a pull request

### Premium Features
Advanced analysis features and proprietary algorithms are private and require a commercial license.
Contact us for licensing information.

## License

### Core Features - MIT License
Copyright (c) 2024 [Your Name]

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software.

### Premium Features
All rights reserved. Contact for licensing information.
