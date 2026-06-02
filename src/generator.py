from openai import OpenAI

client = OpenAI(
    base_url="http://localhost:1234/v1",
    api_key="lm-studio"
)

def generate_answer(
    context,
    question
):

    prompt = f"""
You are a helpful assistant.

Answer ONLY from the context.

Context:
{context}

Question:
{question}

If answer not found,
say:
Information not available.

Answer:
"""

    stream = client.chat.completions.create(
        model="mistral-7b-instruct-v0.1",
        messages=[
            {
                "role": "user",
                "content": prompt
            }
        ],
        stream=True
    )

    return stream