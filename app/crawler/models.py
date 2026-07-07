from typing import Any

from pydantic import BaseModel


class RawPage(BaseModel):
    title: str
    url: str

    markdown: str
    html: str

    metadata: dict[str, Any]

    internal_links: list[dict[str, Any]]
    external_links: list[dict[str, Any]]

    images: list[dict[str, Any]]