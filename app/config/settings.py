from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    # Website
    WEBSITE_URL: str

    # OpenAI
    OPENAI_API_KEY: str
    OPENAI_EMBEDDING_MODEL: str = "text-embedding-3-small"

    # Ollama
    OLLAMA_BASE_URL: str = "http://localhost:11434"
    OLLAMA_MODEL: str = "llama3.2:3b"

    # ChromaDB
    CHROMA_DB_PATH: str = "./data/chroma"
    CHROMA_COLLECTION: str = "website_chunks"

    model_config = SettingsConfigDict(
        env_file=".env",
        extra="ignore",
    )


settings = Settings()