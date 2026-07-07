import json
from pathlib import Path

from app.crawler.models import RawPage

RAW_FILE = Path("data/raw/pages.json")
CLEAN_DIR = Path("data/cleaned")
CLEAN_DIR.mkdir(parents=True, exist_ok=True)

CLEAN_FILE = CLEAN_DIR / "pages.json"


def load_pages() -> list[RawPage]:

    with open(RAW_FILE, "r", encoding="utf-8") as f:

        data = json.load(f)

    return [RawPage(**page) for page in data]


def save_pages(pages: list[RawPage]):

    with open(CLEAN_FILE, "w", encoding="utf-8") as f:

        json.dump(
            [page.model_dump() for page in pages],
            f,
            indent=4,
            ensure_ascii=False,
        )