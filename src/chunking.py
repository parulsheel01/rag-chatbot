from pypdf import PdfReader
from langchain_text_splitters import RecursiveCharacterTextSplitter
import json

def create_chunks(pdf_path):

    reader = PdfReader(pdf_path)

    text = ""

    for page in reader.pages:
        extracted = page.extract_text()

        if extracted:
            text += extracted + "\n"

    splitter = RecursiveCharacterTextSplitter(
        chunk_size=800,
        chunk_overlap=100
    )

    chunks = splitter.split_text(text)

    with open("chunks/chunks.json", "w", encoding="utf-8") as f:
        json.dump(chunks, f, indent=4)

    return chunks