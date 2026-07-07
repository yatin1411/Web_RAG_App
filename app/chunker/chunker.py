import re
import uuid

from langchain_text_splitters import RecursiveCharacterTextSplitter

from app.chunker.models import Chunk
from app.chunker.markdown import split_markdown_sections


splitter = RecursiveCharacterTextSplitter(
    chunk_size=800,
    chunk_overlap=150,
)


def extract_heading(section: str) -> str:

    match = re.match(r"^(#{1,6})\s+(.*)", section)

    if match:
        return match.group(2).strip()

    return "Untitled"


def chunk_page(page):

    chunks = []

    chunk_index = 0

    sections = split_markdown_sections(page.markdown)

    for section in sections:

        heading = extract_heading(section)

        pieces = splitter.split_text(section)

        for piece in pieces:

            chunks.append(
                Chunk(
                    chunk_id=str(uuid.uuid4()),
                    page_title=page.title,
                    page_url=page.url,
                    section_title=heading,
                    chunk_index=chunk_index,
                    content=piece,
                    char_count=len(piece),
                    word_count=len(piece.split()),
                )
            )

            chunk_index += 1

    return chunks