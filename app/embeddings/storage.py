import json
from pathlib import Path

from app.chunker.models import Chunk

CHUNK_FILE = Path("data/chunks/chunks.json")


def load_chunks() -> list[Chunk]:
    with open(CHUNK_FILE, "r", encoding="utf-8") as f:
        data = json.load(f)

    return [Chunk(**chunk) for chunk in data]