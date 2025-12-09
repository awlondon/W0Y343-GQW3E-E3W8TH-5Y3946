"""Generate text-to-speech audio chunks for each chapter file.

This script walks the input directory for Markdown chapter files, splits the text
into manageable chunks, and routes each chunk through a free text-to-speech API
(Google Text-to-Speech via gTTS). Audio is exported as MP3 by default with
optional conversion to WAV or MP4 using pydub/ffmpeg.
"""

from __future__ import annotations

import argparse
import re
from dataclasses import dataclass
from pathlib import Path
from tempfile import NamedTemporaryFile
from typing import Iterable, List

from gtts import gTTS
from pydub import AudioSegment


# Maximum characters per chunk to stay under gTTS limits while avoiding long requests.
DEFAULT_CHUNK_SIZE = 2800
SUPPORTED_FORMATS = {"mp3", "wav", "mp4"}


@dataclass
class GenerationSettings:
    input_dir: Path
    output_dir: Path
    language: str
    chunk_size: int
    audio_format: str


def strip_markdown(text: str) -> str:
    """Remove lightweight Markdown artifacts that can confuse pronunciation."""

    without_code = re.sub(r"`[^`]*`", "", text)
    without_links = re.sub(r"\[[^\]]*\]\([^)]*\)", lambda m: m.group(0).split("]")[0][1:], without_code)
    without_headers = re.sub(r"^#+\s+", "", without_links, flags=re.MULTILINE)
    without_emphasis = re.sub(r"[*_]{1,3}([^*_]+)[*_]{1,3}", r"\1", without_headers)
    cleaned = re.sub(r">\s?", "", without_emphasis)
    collapsed = re.sub(r"\n{2,}", "\n", cleaned)
    return collapsed.strip()


def chunk_text(text: str, max_chars: int) -> List[str]:
    """Split text into chunks that do not exceed ``max_chars``.

    Paragraphs are grouped together until the limit is hit to avoid splitting
    sentences mid-stream.
    """

    paragraphs = [p.strip() for p in text.split("\n") if p.strip()]
    chunks: List[str] = []
    current: List[str] = []
    current_len = 0

    for paragraph in paragraphs:
        para_len = len(paragraph)
        if para_len > max_chars:
            # Extremely long paragraphs are split on sentences.
            sentences = re.split(r"(?<=[.!?])\s+", paragraph)
            for sentence in sentences:
                if not sentence:
                    continue
                sentence_len = len(sentence)
                if current_len + sentence_len <= max_chars:
                    current.append(sentence)
                    current_len += sentence_len + 1
                else:
                    if current:
                        chunks.append(" ".join(current))
                    chunks.append(sentence)
                    current = []
                    current_len = 0
            continue

        if current_len + para_len <= max_chars:
            current.append(paragraph)
            current_len += para_len + 1
        else:
            chunks.append(" ".join(current))
            current = [paragraph]
            current_len = para_len

    if current:
        chunks.append(" ".join(current))

    return chunks


def synthesize_chunk(text: str, language: str, destination: Path, audio_format: str) -> None:
    """Send a chunk through gTTS and export to the requested format."""

    audio_format = audio_format.lower()
    with NamedTemporaryFile(suffix=".mp3", delete=False) as temp_mp3:
        gTTS(text=text, lang=language, slow=False).save(temp_mp3.name)
        temp_path = Path(temp_mp3.name)

    if audio_format == "mp3":
        destination.write_bytes(Path(temp_path).read_bytes())
        return

    audio = AudioSegment.from_mp3(temp_path)
    audio.export(destination, format=audio_format)


def convert_chapters(settings: GenerationSettings) -> None:
    settings.output_dir.mkdir(parents=True, exist_ok=True)
    chapter_paths = sorted(settings.input_dir.glob("Chapter-*.md"))

    for chapter_path in chapter_paths:
        text = chapter_path.read_text(encoding="utf-8")
        normalized = strip_markdown(text)
        chunks = chunk_text(normalized, settings.chunk_size)

        for index, chunk in enumerate(chunks, start=1):
            output_name = f"{chapter_path.stem}-chunk-{index}.{settings.audio_format}"
            destination = settings.output_dir / output_name
            synthesize_chunk(chunk, settings.language, destination, settings.audio_format)
            print(f"Created {destination.relative_to(Path.cwd())}")


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description="Convert chapter Markdown files to TTS audio chunks.")
    parser.add_argument("--input-dir", type=Path, default=Path("Book-1"), help="Directory containing Chapter-*.md files")
    parser.add_argument("--output-dir", type=Path, default=Path("audio"), help="Where to save generated audio")
    parser.add_argument("--language", default="en", help="Language code for gTTS (default: en)")
    parser.add_argument("--chunk-size", type=int, default=DEFAULT_CHUNK_SIZE, help=f"Max characters per chunk (default: {DEFAULT_CHUNK_SIZE})")
    parser.add_argument("--format", choices=sorted(SUPPORTED_FORMATS), default="wav", help="Output audio format")
    return parser


def main(args: Iterable[str] | None = None) -> None:
    parser = build_parser()
    parsed = parser.parse_args(args=args)
    settings = GenerationSettings(
        input_dir=parsed.input_dir,
        output_dir=parsed.output_dir,
        language=parsed.language,
        chunk_size=parsed.chunk_size,
        audio_format=parsed.format,
    )
    convert_chapters(settings)


if __name__ == "__main__":
    main()
