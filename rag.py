from langchain_community.vectorstores import FAISS
from langchain_aws import BedrockEmbeddings
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_community.document_loaders import PyPDFLoader
import os

VECTOR_DB_PATH = "vectorstore/faiss_index"

def build_vector_db():
    docs = []

    for file in os.listdir("data/documents"):
        if file.endswith(".pdf"):
            loader = PyPDFLoader(f"data/documents/{file}")
            docs.extend(loader.load())

    splitter = RecursiveCharacterTextSplitter(
        chunk_size=500,
        chunk_overlap=100
    )
    chunks = splitter.split_documents(docs)

    embeddings = BedrockEmbeddings(
        model_id="amazon.titan-embed-text-v1",
        region_name="us-east-1"
    )

    vectorstore = FAISS.from_documents(chunks, embeddings)
    vectorstore.save_local(VECTOR_DB_PATH)
    print("✅ Vector database built and saved.")

def get_retriever():
    embeddings = BedrockEmbeddings(
        model_id="amazon.titan-embed-text-v1",
        region_name="us-east-1"
    )

    vectorstore = FAISS.load_local(
        VECTOR_DB_PATH,
        embeddings,
        allow_dangerous_deserialization=True
    )

    return vectorstore.as_retriever(search_kwargs={"k": 3})


if __name__ == "__main__":
    build_vector_db()