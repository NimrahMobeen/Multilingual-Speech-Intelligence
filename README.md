# TTS Audio Processing API

Production-grade audio processing API with support for transcription, translation, speaker analysis, and audio classification.

## Features

- 🎤 **Multi-language Transcription** (Whisper) - Urdu, Dari, Pashto, Arabic, English
- 🌐 **Translation** - NLLB-based translation with Pashto normalization
- 👥 **Speaker Diarization** - Identify and separate speakers
- 🔊 **Audio Analysis** - Background sound classification, pause detection
- 🎭 **Emotion Detection** - Analyze speaker emotions
- 🔍 **Voice Matching** - Speaker verification against gallery
- 📊 **Text Analytics** - NER, summarization, statistics

## Prerequisites

- Python 3.9+
- CUDA-capable GPU (recommended)
- FFmpeg
- Docker (optional, for containerized deployment)

## Quick Start

### 1. Clone and Setup

```bash
cd c:\Users\Office\tts
```

### 2. Create Virtual Environment

```bash
python -m venv venv
venv\Scripts\activate  # Windows
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

### 4. Configure Environment

```bash
# Copy example env file
copy .env.example .env

# Edit .env and add your Hugging Face token
# HF_TOKEN=your_actual_token_here
```

### 5. Download Models

Place your model files in the following structure:
```
models/
├── whisper-large-v3/
├── nllb/
├── mt5summarizer/
└── ...
```

Or run the download script:
```bash
python scripts/download_models.py
```

### 6. Run the API

```bash
python main.py
```

The API will be available at: `http://localhost:5000`

API documentation: `http://localhost:5000/docs`

## Docker Deployment (Optional)

### Build and Run

```bash
cd infra/docker
docker-compose up -d
```

### With GPU Support

```bash
docker-compose up -d
```

The docker-compose.yml already includes GPU passthrough configuration.

## API Usage

### Get Available Languages

```bash
curl http://localhost:5000/getlanguages
```

### Get Available Actions

```bash
curl http://localhost:5000/getactions
```

### Process Audio

```bash
curl -X POST http://localhost:5000/process_audio \
  -F "file=@audio.mp3" \
  -F "language=Urdu" \
  -F "action=Show Transcript" \
  -F "model=large"
```

### Available Actions

- `Show Transcript` - Get transcription
- `Translate to English` - Transcribe + translate
- `Show Statistics` - Word count, frequency analysis
- `Extract Key Info` - Named entity recognition
- `Show Summary` - Text summarization
- `Get Emotions` - Emotion analysis
- `Analyze Background` - Background sound classification
- `Speaker Biographics` - Age/gender prediction
- `Detect Pause` - Pause detection with timestamps
- `Voice Matching` - Speaker verification
- `Diarization` - Multi-speaker transcription

## Project Structure

```
tts/
├── api/              # FastAPI routes and schemas
├── config/           # Configuration and constants
├── core/             # Core functionality (models, DI)
├── services/         # Business logic services
├── utils/            # Helper utilities
├── infra/            # Docker and infrastructure
├── models/           # ML model artifacts (gitignored)
├── scripts/          # Utility scripts
└── main.py           # Application entry point
```

## Configuration

Edit `.env` file to configure:

- `HF_TOKEN` - Hugging Face API token (required)
- `DEVICE` - GPU device (cuda:0, cuda:1, or cpu)
- `NUM_GPUS` - Number of GPUs available
- `PORT` - API port (default: 5000)
- `DEBUG` - Debug mode (True/False)
- `LAZY_LOAD_MODELS` - Load models on-demand vs at startup

## Monitoring

Basic Prometheus metrics available at: `http://localhost:5000/metrics`

View with Prometheus (if using docker-compose):
```bash
http://localhost:9090
```

## Development

### Code Style

The project follows Python best practices:
- Black for formatting
- isort for import sorting
- Type hints throughout

### Adding New Features

1. Add service logic in `services/`
2. Define API schemas in `api/schemas.py`
3. Add route in `api/routes.py`
4. Update documentation

## Troubleshooting

### CUDA Out of Memory

- Reduce batch size in transcription
- Enable `LAZY_LOAD_MODELS=True`
- Use smaller model variants

### Models Not Loading

- Check model paths in settings
- Verify HF_TOKEN is correct
- Ensure models are downloaded

### Audio Processing Errors

- Verify FFmpeg is installed
- Check audio file format (supports: mp3, wav, flac, ogg)
- Check file permissions

## License

[Your License Here]

## Support

For issues and questions, please open an issue on the repository.
