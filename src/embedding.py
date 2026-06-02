import json
import faiss
import numpy as np

from sentence_transformers import SentenceTransformer

EMBED_MODEL = SentenceTransformer(
    "sentence-transformers/all-MiniLM-L6-v2"
)

def build_vector_db():

    with open(
        "chunks/chunks.json",
        "r",
        encoding="utf-8"
    ) as f:

        chunks = json.load(f)

    embeddings = EMBED_MODEL.encode(chunks)

    embeddings = np.array(
        embeddings,
        dtype="float32"
    )

    dimension = embeddings.shape[1]

    index = faiss.IndexFlatL2(dimension)

    index.add(embeddings)

    faiss.write_index(
        index,
        "vectordb/faiss.index"
    )

    return chunks