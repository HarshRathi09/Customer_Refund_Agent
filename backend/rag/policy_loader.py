from pathlib import Path

from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_core.documents import Document


BASE_DIR = Path(__file__).resolve().parent.parent

POLICY_FILE = BASE_DIR / "data" / "refund_policy.txt"


def load_policy():

    with open(
        POLICY_FILE,
        "r",
        encoding="utf-8"
    ) as f:
        policy_text = f.read()

    splitter = RecursiveCharacterTextSplitter(
        chunk_size=300,
        chunk_overlap=50
    )

    documents = splitter.split_documents(
        [
            Document(
                page_content=policy_text
            )
        ]
    )

    return documents