from app.embeddings.embedder import generate_embeddings
from app.embeddings.chroma import collection


BATCH_SIZE = 50


def index_chunks(chunks):

    for i in range(0, len(chunks), BATCH_SIZE):

        batch = chunks[i:i+BATCH_SIZE]

        texts = [
            chunk.content
            for chunk in batch
        ]

        embeddings = generate_embeddings(texts)

        ids = [
            chunk.chunk_id
            for chunk in batch
        ]

        documents = texts

        metadatas = []

        for chunk in batch:

            metadatas.append(
                {
                    "page_title": chunk.page_title,
                    "page_url": chunk.page_url,
                    "section_title": chunk.section_title,
                    "chunk_index": chunk.chunk_index,
                    "char_count": chunk.char_count,
                    "word_count": chunk.word_count,
                }
            )

        collection.add(
            ids=ids,
            documents=documents,
            embeddings=embeddings,
            metadatas=metadatas,
        )

        print(
            f"Indexed {min(i+BATCH_SIZE, len(chunks))}/{len(chunks)} chunks"
        )