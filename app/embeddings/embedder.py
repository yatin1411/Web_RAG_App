from openai import OpenAI

from app.config.settings import settings

client = OpenAI(api_key=settings.OPENAI_API_KEY)


def generate_embeddings(texts: list[str]) -> list[list[float]]:
    """
    Generate embeddings for multiple texts.
    """

    response = client.embeddings.create(
        model=settings.OPENAI_EMBEDDING_MODEL,
        input=texts,
    )

    return [item.embedding for item in response.data]