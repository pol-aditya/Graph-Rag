#.........   earlier
# from sentence_transformers import SentenceTransformer

# model = SentenceTransformer('all-MiniLM-L6-v2')

# def generate_embeddings(chunks):

#     embeddings = model.encode(chunks)

#     return embeddings


from sentence_transformers import SentenceTransformer

model = SentenceTransformer('all-MiniLM-L6-v2')

def generate_embeddings(chunks):

    embeddings = model.encode(chunks)

    return embeddings


def generate_query_embedding(query):

    return model.encode(query)

# Earlier:

# document chunks → embeddings

# Now:

# user question → embedding