import chromadb

from llama_index.core import (
    VectorStoreIndex,
    Settings,
)

from llama_index.embeddings.huggingface import HuggingFaceEmbedding
from llama_index.vector_stores.chroma import ChromaVectorStore


# --------------------------------------------------
# Embedding model
# --------------------------------------------------

Settings.embed_model = HuggingFaceEmbedding(
    model_name="BAAI/bge-small-en-v1.5"
)


# --------------------------------------------------
# Connect to Chroma
# --------------------------------------------------

chroma_client = chromadb.PersistentClient(
    path="./chroma_db"
)

collection = chroma_client.get_collection(
    name="medcore_rag"
)

vector_store = ChromaVectorStore(
    chroma_collection=collection
)


# --------------------------------------------------
# Load index
# --------------------------------------------------

index = VectorStoreIndex.from_vector_store(
    vector_store
)


# --------------------------------------------------
# Retriever
# --------------------------------------------------

retriever = index.as_retriever(
    similarity_top_k=10
)


# --------------------------------------------------
# Ask question
# --------------------------------------------------

question = input("\nAsk your question: ")

results = retriever.retrieve(question)


print("\n")
print("=" * 70)
print("RETRIEVED INFORMATION")
print("=" * 70)


for i, result in enumerate(results, start=1):

    print()
    print(f"RESULT {i}")
    print("-" * 70)

    print(result.node.text[:1200])

    print()
    print("Department:",
          result.node.metadata.get("department"))

    print("File:",
          result.node.metadata.get("file_name"))

    print("Document type:",
          result.node.metadata.get("document_type"))
