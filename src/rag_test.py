import chromadb

from llama_index.core import VectorStoreIndex, Settings
from llama_index.embeddings.huggingface import HuggingFaceEmbedding
from llama_index.vector_stores.chroma import ChromaVectorStore
from llama_index.llms.ollama import Ollama


# --------------------------------------------------
# 1. Embedding model
# --------------------------------------------------

Settings.embed_model = HuggingFaceEmbedding(
    model_name="BAAI/bge-small-en-v1.5"
)


# --------------------------------------------------
# 2. Ollama Cloud LLM
# --------------------------------------------------

Settings.llm = Ollama(
    model="gpt-oss:20b-cloud",
    request_timeout=120.0,
)


# --------------------------------------------------
# 3. Connect to existing Chroma database
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
# 4. Reconnect LlamaIndex to Chroma
# --------------------------------------------------

index = VectorStoreIndex.from_vector_store(
    vector_store
)


# --------------------------------------------------
# 5. Create RAG query engine
# --------------------------------------------------

query_engine = index.as_query_engine(
    similarity_top_k=5
)


# --------------------------------------------------
# 6. Ask question
# --------------------------------------------------

question = input("\nAsk your question: ")

response = query_engine.query(question)


# --------------------------------------------------
# 7. Display ONE final answer
# --------------------------------------------------

print("\n")
print("=" * 70)
print("MEDCORE RAG ANSWER")
print("=" * 70)

print(response)

print("\n")
print("=" * 70)
print("SOURCES")
print("=" * 70)

for source in response.source_nodes:
    metadata = source.node.metadata

    print(
        f"- {metadata.get('department')} | "
        f"{metadata.get('file_name')}"
    )
