from rag_pipeline import chunk_text
from pdf_loader import load_pdf

text = load_pdf("sample.pdf")

chunks = chunk_text(text)

print(chunks[0])

# test chunking
