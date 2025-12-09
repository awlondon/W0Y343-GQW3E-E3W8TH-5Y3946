# Chapter Text-to-Speech Generator

This repository includes a helper script to turn the `Chapter-*.md` files into text-to-speech audio chunks using the free [gTTS](https://pypi.org/project/gTTS/) API. Audio can be exported as MP3, WAV, or MP4 files.

## Setup

1. Install Python 3.10+.
2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
3. For WAV or MP4 output, ensure [`ffmpeg`](https://ffmpeg.org/) is available on your system (required by `pydub`).

## Usage

Generate WAV files for every chapter into an `audio/` folder (default behavior):

```bash
python generate_tts_audio.py
```

Common options:

- Choose output format:
  ```bash
  python generate_tts_audio.py --format mp3
  ```
- Save files to a custom directory:
  ```bash
  python generate_tts_audio.py --output-dir builds/audio
  ```
- Adjust chunk size (max characters per TTS request):
  ```bash
  python generate_tts_audio.py --chunk-size 3200
  ```
- Process a different input folder:
  ```bash
  python generate_tts_audio.py --input-dir Book-1
  ```

The script will print each generated chunk, e.g., `Created audio/Chapter-1-chunk-1.wav`. Combine the chunks in your preferred editor if you need single, long-form audio files.
