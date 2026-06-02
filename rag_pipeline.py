# CHUNKING

def chunk_text(text, chunk_size=500):

    chunks = []

    for i in range(0, len(text), chunk_size):
        chunk = text[i:i + chunk_size]
        chunks.append(chunk)

    return chunks
# */
# WHAT THIS DOES

# Big document:

# 100 pages

# becomes:

# small manageable chunks
# /*