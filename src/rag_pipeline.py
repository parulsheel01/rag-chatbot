from src.retriever import retrieve
from src.generator import generate_answer

def run_rag(query):

    retrieved_chunks = retrieve(query)

    context = "\n\n".join(
        retrieved_chunks
    )

    stream = generate_answer(
        context,
        query
    )

    return stream, retrieved_chunks