import chromadb

from app.config.settings import settings

client = chromadb.PersistentClient(
    path=settings.CHROMA_DB_PATH
)

collection = client.get_or_create_collection(
    name=settings.CHROMA_COLLECTION
)