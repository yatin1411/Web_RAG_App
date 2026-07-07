from pydantic import BaseModel


class Chunk(BaseModel):
    chunk_id: str

    page_title: str
    page_url: str

    section_title: str

    chunk_index: int

    content: str

    char_count: int
    word_count: int