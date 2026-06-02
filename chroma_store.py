# WHAT THIS DOES

# Suppose user asks:

# "What projects are in the resume?"

# ChromaDB searches:

# which chunks are semantically similar

# and returns top matching chunks.
import chromadb

client = chromadb.Client()

collection = client.get_or_create_collection("rag_collection")


def store_chunks(chunks, embeddings):

    for i, chunk in enumerate(chunks):

        collection.add(
            ids=[str(i)],
            documents=[chunk],
            embeddings=[embeddings[i].tolist()]
        )


def retrieve_chunks(query_embedding):

    results = collection.query(
        query_embeddings=[query_embedding.tolist()],
        n_results=3
    )

    return results
# # CHROMA DB

# What ChromaDB does

# Stores:

# embedding vectors

# and allows:

# similarity search