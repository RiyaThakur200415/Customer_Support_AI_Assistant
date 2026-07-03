import os

from langchain_community.vectorstores import FAISS
from langchain_ollama import OllamaEmbeddings

VECTOR_DB_PATH = "rag/faiss_index"


def retrieve_context(query):

    # Check if vector database exists
    if not os.path.exists(VECTOR_DB_PATH):
        return "Vector database not found. Please run: python rag/vector_store.py"

    try:
        embeddings = OllamaEmbeddings(
            model="nomic-embed-text"
        )

        db = FAISS.load_local(
            VECTOR_DB_PATH,
            embeddings,
            allow_dangerous_deserialization=True
        )

        retriever = db.as_retriever(
            search_kwargs={"k": 3}
        )

        docs = retriever.invoke(query)

        if not docs:
            return "No relevant information found."

        context = "\n\n".join(
            doc.page_content for doc in docs
        )

        return context

    except Exception as e:
        print("RAG Error:", e)
        return f"Unable to retrieve context: {str(e)}"