import json
from pathlib import Path

from app.crawler.models import RawPage

RAW_FOLDER = Path("data/raw")
RAW_FOLDER.mkdir(parents=True, exist_ok=True)


def save_pages(pages: list[RawPage]):

    with open(RAW_FOLDER / "pages.json", "w", encoding="utf-8") as f:

        json.dump(
            [page.model_dump() for page in pages],
            f,
            indent=4,
            ensure_ascii=False,
        )