import json
import faiss
import numpy as np

from sentence_transformers import SentenceTransformer

EMBED_MODEL = SentenceTransformer(
    "sentence-transformers/all-MiniLM-L6-v2"
)

index = faiss.read_index(
    "vectordb/faiss.index"
)

with open(
    "chunks/chunks.json",
    "r",
    encoding="utf-8"
) as f:

    chunks = json.load(f)

def retrieve(query, k=3):

    query_embedding = EMBED_MODEL.encode([query])

    query_embedding = np.array(
        query_embedding,
        dtype="float32"
    )

    distances, indices = index.search(
        query_embedding,
        k
    )

    results = []

    for idx in indices[0]:
        results.append(chunks[idx])

    return results