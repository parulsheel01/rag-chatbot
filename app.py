# import streamlit as st

# from src.rag_pipeline import run_rag

# st.set_page_config(
#     page_title="RAG Chatbot"
# )

# st.title("📄 RAG Chatbot")

# question = st.chat_input(
#     "Ask a question..."
# )

# if question:

#     st.chat_message(
#         "user"
#     ).write(question)

#     stream, sources = run_rag(
#         question
#     )

#     response = ""

#     placeholder = st.empty()

#     for chunk in stream:

#         token = (
#             chunk
#             .choices[0]
#             .delta
#             .content
#         )

#         if token:

#             response += token

#             placeholder.markdown(
#                 response
#             )

#     with st.expander(
#         "Source Chunks"
#     ):

#         for source in sources:
#             st.write(source)

import streamlit as st

from src.rag_pipeline import run_rag

st.set_page_config(
    page_title="RAG Chatbot"
)

st.title("📄 RAG Chatbot")

# Initialize chat history

if "messages" not in st.session_state:
    st.session_state.messages = []

# Display old messages

for message in st.session_state.messages:

    with st.chat_message(
        message["role"]
    ):
        st.markdown(
            message["content"]
        )

# User input

question = st.chat_input(
    "Ask a question..."
)

if question:

    # Save user message

    st.session_state.messages.append(
        {
            "role": "user",
            "content": question
        }
    )

    # Display user message

    with st.chat_message("user"):
        st.markdown(question)

    # Run RAG

    stream, sources = run_rag(
        question
    )

    response = ""

    with st.chat_message("assistant"):

        placeholder = st.empty()

        for chunk in stream:

            token = (
                chunk
                .choices[0]
                .delta
                .content
            )

            if token:

                response += token

                placeholder.markdown(
                    response
                )

    # Save assistant response

    st.session_state.messages.append(
        {
            "role": "assistant",
            "content": response
        }
    )

    # Show sources

    with st.expander(
        "Source Chunks"
    ):

        for source in sources:
            st.write(source)

# Clear chat button

if st.sidebar.button(
    "🗑️ Clear Chat"
):

    st.session_state.messages = []

    st.rerun()