import chromadb

from llama_index.core import (
    VectorStoreIndex,
    StorageContext,
    Settings,
)

from llama_index.embeddings.huggingface import HuggingFaceEmbedding
from llama_index.vector_stores.chroma import ChromaVectorStore


# --------------------------------------------------
# 1. Embedding model
# --------------------------------------------------

Settings.embed_model = HuggingFaceEmbedding(
    model_name="BAAI/bge-small-en-v1.5"
)


# --------------------------------------------------
# 2. Connect to existing Chroma database
# --------------------------------------------------

chroma_client = chromadb.PersistentClient(
    path="./chroma_db"
)

collection = chroma_client.get_collection(
    name="medcore_test"
)

vector_store = ChromaVectorStore(
    chroma_collection=collection
)


# --------------------------------------------------
# 3. Reconnect LlamaIndex to Chroma
# --------------------------------------------------

index = VectorStoreIndex.from_vector_store(
    vector_store
)


# --------------------------------------------------
# 4. Create retriever
# --------------------------------------------------

retriever = index.as_retriever(
    similarity_top_k=3
)


# --------------------------------------------------
# 5. Ask a question
# --------------------------------------------------

question = "What is the procedure for patient admission?"

results = retriever.retrieve(question)


print()
print("=" * 60)
print("QUESTION:")
print(question)
print("=" * 60)

for i, result in enumerate(results, start=1):

    print()
    print(f"RESULT {i}")
    print("-" * 60)

    print(result.node.text[:1500])

    print()
    print("Metadata:")
    print(result.node.metadata)
