from embeddings import generate_embeddings

chunks = ["camera permission", "privacy policy"]

vectors = generate_embeddings(chunks)

print(vectors.shape)