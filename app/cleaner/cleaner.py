import re
import unicodedata


def clean_markdown(text: str) -> str:
    """
    Cleans markdown text before chunking.
    """

    if not text:
        return ""

    # Normalize unicode
    text = unicodedata.normalize("NFKC", text)

    # Remove zero-width characters
    text = re.sub(r"[\u200B-\u200D\uFEFF]", "", text)

    # Replace tabs with spaces
    text = text.replace("\t", " ")

    # Replace multiple spaces
    text = re.sub(r"[ ]{2,}", " ", text)

    # Remove trailing spaces
    text = re.sub(r"[ \t]+\n", "\n", text)

    # Collapse multiple blank lines
    text = re.sub(r"\n{3,}", "\n\n", text)

    return text.strip()