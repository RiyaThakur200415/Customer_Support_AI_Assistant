from langchain_community.document_loaders import DirectoryLoader, TextLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_ollama import OllamaEmbeddings
from langchain_community.vectorstores import FAISS

DOCUMENT_PATH = "rag/documents"
VECTOR_DB_PATH = "rag/faiss_index"


def create_vector_store():

    loader = DirectoryLoader(
        DOCUMENT_PATH,
        glob="*.txt",
        loader_cls=TextLoader
    )

    documents = loader.load()

    splitter = RecursiveCharacterTextSplitter(
        chunk_size=500,
        chunk_overlap=100
    )

    chunks = splitter.split_documents(documents)

    embeddings = OllamaEmbeddings(
    model="nomic-embed-text"
)

    db = FAISS.from_documents(
        chunks,
        embeddings
    )

    db.save_local(VECTOR_DB_PATH)

    print("Vector Store Created Successfully")


if __name__ == "__main__":
    create_vector_store()