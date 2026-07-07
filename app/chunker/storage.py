import json
from pathlib import Path

from app.chunker.models import Chunk
from app.crawler.models import RawPage


CLEAN_FILE = Path("data/cleaned/pages.json")

CHUNK_DIR = Path("data/chunks")
CHUNK_DIR.mkdir(parents=True, exist_ok=True)

CHUNK_FILE = CHUNK_DIR / "chunks.json"


def load_pages():

    with open(CLEAN_FILE, "r", encoding="utf-8") as f:

        data = json.load(f)

    return [RawPage(**page) for page in data]


def save_chunks(chunks: list[Chunk]):

    with open(CHUNK_FILE, "w", encoding="utf-8") as f:

        json.dump(
            [chunk.model_dump() for chunk in chunks],
            f,
            indent=4,
            ensure_ascii=False,
        )