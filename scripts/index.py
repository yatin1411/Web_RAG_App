from app.embeddings.storage import load_chunks
from app.embeddings.indexer import index_chunks


def main():

    chunks = load_chunks()

    print(f"Loaded {len(chunks)} chunks")

    index_chunks(chunks)

    print("Indexing completed.")


if __name__ == "__main__":
    main()