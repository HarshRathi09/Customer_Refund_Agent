from pathlib import Path

from langchain_community.vectorstores import FAISS
from langchain_huggingface import HuggingFaceEmbeddings

from rag.policy_loader import load_policy


BASE_DIR = Path(__file__).resolve().parent.parent

VECTOR_DB_PATH = BASE_DIR / "policy_faiss"

EMBEDDINGS = HuggingFaceEmbeddings(
    model_name="sentence-transformers/all-MiniLM-L6-v2"
)

def create_vectorstore():

    docs = load_policy()

    vectorstore = FAISS.from_documents(
        docs,
        EMBEDDINGS
    )

    vectorstore.save_local(
        str(VECTOR_DB_PATH)
    )

    print(
        f"Vector store saved to {VECTOR_DB_PATH}"
    )

    return vectorstore

def load_vectorstore():

    return FAISS.load_local(
        str(VECTOR_DB_PATH),
        EMBEDDINGS,
        allow_dangerous_deserialization=True
    )