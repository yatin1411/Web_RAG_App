from app.chunker.chunker import chunk_page
from app.chunker.storage import load_pages, save_chunks


def main():

    pages = load_pages()

    all_chunks = []

    for page in pages:

        chunks = chunk_page(page)

        all_chunks.extend(chunks)

    save_chunks(all_chunks)

    print(f"Created {len(all_chunks)} chunks")


if __name__ == "__main__":
    main()