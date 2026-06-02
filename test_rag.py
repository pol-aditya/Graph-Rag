# from entity_extractor import extract_entities

# from neo4j_graph import get_graph_context

# from knowledge_graph import query_graph
# from entity_extractor import extract_entities
# from entity_extractor import extract_entities
# from knowledge_graph import query_graph
# from audit_retrieval import calculate_chunk_score
# from code_loader import load_code_file # for loading code files
# code_text = load_code_file("sample_app_code.txt") # load LOAD SOURCE CODE
# from pdf_loader import load_pdf
# from rag_pipeline import chunk_text
# from embeddings import generate_embeddings, generate_query_embedding
# from chroma_store import store_chunks, retrieve_chunks
# from llm import ask_llm
# # COMBINE WITH PDF TEXT
# pdf_text = load_pdf("sample.pdf")

# code_text = load_code_file("sample_app_code.txt")

# text = pdf_text + "\n\n" + code_text
# # what above does ---> Your RAG system receives:

# #  Privacy Policy
# # +
# # Source Code

# # TOGETHER.

# # 

# # Chunking
# chunks = chunk_text(text)
# # chunk scoreing
# scored_chunks = []

# # for chunk in chunks:

# #     score = calculate_chunk_score(chunk, "privacy_policy.pdf")

# #     scored_chunks.append((chunk, score))
    
# #     # SORT BY SCORE
# #     scored_chunks.sort(key=lambda x: x[1], reverse=True)
    
#     # top chunks 
#     top_chunks = [chunk for chunk, score in scored_chunks[:10]]
#     # GENERATE EMBEDDINGS USING TOP CHUNKS
#     # Generate embeddings
#     embeddings = generate_embeddings(top_chunks)

# # Store chunks
# store_chunks(top_chunks, embeddings)

# print("Chunks stored successfully!")


# # User question
# question = "What privacy risks exist?"

# # Generate query embedding
# query_embedding = generate_query_embedding(question)

# # Retrieve relevant chunks
# results = retrieve_chunks(query_embedding)

# retrieved_docs = results['documents'][0]
# # for knowldge graph context

# # from retrieved content.

# # Then queries graph for EACH entity.
    
# context = "\n".join(retrieved_docs)

# # Extract entities from retrieved context
# entities = extract_entities(context)

# graph_data = {}

# for entity in entities:

#     graph_data[entity] = get_graph_context(entity)
# #     🚀 WHAT THIS  above DOES

# # Suppose retrieved context contains:

# # camera
# # location
# # tracking

# entities = extract_entities(context)

# graph_context = {}

# # for entity in entities:

# #     graph_context[entity] = query_graph(entity)
# # #     🚀 WHAT HAPPENS NOW by above 

# # System dynamically detects:

# # camera
# # location
# # analytics

# # STEP 5 — APPEND GRAPH KNOWLEDGE
# context += f"\n\nGraph Knowledge:\n{graph_data}"


# context += f"\n\nGraph Knowledge:\n{graph_context}"

# print("\nRetrieved Context:\n")
# print(context)

# print("\nGenerating Answer...\n")

# # open router api key using ans  answer (send to llm)
# answer = ask_llm(context, question)
# print(answer)

# /////////////////////below one is correct one 




# =========================================================
# IMPORTS
# =========================================================

# Extract important entities like:
# camera, location, analytics
from entity_extractor import extract_entities


# Get graph relationships from Neo4j
# Example:
# camera -> GDPR
# camera -> User Consent
from neo4j_graph import get_graph_context


# Used for keyword-based chunk scoring
# Helps prioritize important privacy chunks
from audit_retrieval import calculate_chunk_score


# Load source code file
from code_loader import load_code_file


# Load PDF privacy policy
from pdf_loader import load_pdf


# Split large text into smaller chunks
from rag_pipeline import chunk_text


# Generate vector embeddings
from embeddings import (
    generate_embeddings,
    generate_query_embedding
)


# Store + retrieve chunks from ChromaDB
from chroma_store import (
    store_chunks,
    retrieve_chunks
)


# Send final context to LLM
from llm import ask_llm


# =========================================================
# STEP 1 — LOAD DATA
# =========================================================

# Load privacy policy PDF
pdf_text = load_pdf("sample.pdf")


# Load sample app source code
code_text = load_code_file(
    "sample_app_code.txt"
)


# Combine BOTH together
# So RAG receives:
# Privacy Policy + Source Code
text = pdf_text + "\n\n" + code_text


# =========================================================
# STEP 2 — CHUNKING
# =========================================================

# Split large combined text
# into smaller manageable chunks
chunks = chunk_text(text)


# =========================================================
# STEP 3 — CHUNK SCORING
# =========================================================

# Goal:
# prioritize privacy/security chunks

scored_chunks = []

for chunk in chunks:

    # Calculate chunk importance score
    score = calculate_chunk_score(
        chunk,
        "privacy_policy.pdf"
    )

    # Store:
    # (chunk, score)
    scored_chunks.append(
        (chunk, score)
    )


# =========================================================
# STEP 4 — SORT CHUNKS
# =========================================================

# Higher score first
scored_chunks.sort(
    key=lambda x: x[1],
    reverse=True
)


# =========================================================
# STEP 5 — SELECT TOP CHUNKS
# =========================================================

# Keep only most important chunks
top_chunks = [
    chunk for chunk, score in scored_chunks[:10]
]


# =========================================================
# STEP 6 — GENERATE EMBEDDINGS
# =========================================================

# Convert chunks into vectors
embeddings = generate_embeddings(
    top_chunks
)


# =========================================================
# STEP 7 — STORE IN CHROMADB
# =========================================================

store_chunks(
    top_chunks,
    embeddings
)

print("Chunks stored successfully!")


# =========================================================
# STEP 8 — USER QUESTION
# =========================================================

question = (
    "What privacy risks exist?"
)


# =========================================================
# STEP 9 — QUESTION EMBEDDING
# =========================================================

# Convert user question into vector
query_embedding = generate_query_embedding(
    question
)


# =========================================================
# STEP 10 — RETRIEVE RELEVANT CHUNKS
# =========================================================

results = retrieve_chunks(
    query_embedding
)


# Extract retrieved documents
retrieved_docs = results['documents'][0]


# =========================================================
# STEP 11 — CREATE CONTEXT
# =========================================================

# Combine retrieved chunks into one string
context = "\n".join(
    retrieved_docs
)


# =========================================================
# STEP 12 — ENTITY EXTRACTION
# =========================================================

# Detect entities like:
# camera, location, analytics
entities = extract_entities(
    context
)


# =========================================================
# STEP 13 — NEO4J GRAPH RETRIEVAL
# =========================================================

# Store graph relationships
graph_data = {}

for entity in entities:

    # Query Neo4j graph DB
    graph_data[entity] = (
        get_graph_context(entity)
    )


# =========================================================
# STEP 14 — APPEND GRAPH KNOWLEDGE
# =========================================================

# Add graph relationships into context
context += (
    f"\n\nGraph Knowledge:\n{graph_data}"
)


# =========================================================
# STEP 15 — PRINT RETRIEVED CONTEXT
# =========================================================

print("\nRetrieved Context:\n")

print(context)


# =========================================================
# STEP 16 — SEND TO LLM
# =========================================================

print("\nGenerating Answer...\n")


# Send:
# context + question
# to LLM
answer = ask_llm(
    context,
    question
)


# =========================================================
# STEP 17 — FINAL OUTPUT
# =========================================================

print(answer)
