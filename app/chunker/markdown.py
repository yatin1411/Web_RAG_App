import re


def split_markdown_sections(markdown: str):
    """
    Splits markdown into sections using headings.
    """

    if not markdown.strip():
        return []

    pattern = r"(?=^#{1,6}\s)"

    sections = re.split(pattern, markdown, flags=re.MULTILINE)

    sections = [section.strip() for section in sections if section.strip()]

    return sections