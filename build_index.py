from src.chunking import create_chunks
from src.embedding import build_vector_db

pdf_path = "data/AI Training Document.pdf"

create_chunks(pdf_path)

build_vector_db()

print("Index created.")