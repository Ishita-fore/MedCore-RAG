import chromadb
from llama_index.core import VectorStoreIndex, Settings
from llama_index.embeddings.huggingface import HuggingFaceEmbedding
from llama_index.vector_stores.chroma import ChromaVectorStore
from llama_index.llms.ollama import Ollama

Settings.embed_model = HuggingFaceEmbedding(
    model_name="BAAI/bge-small-en-v1.5"
)

Settings.llm = Ollama(
    model="gpt-oss:20b-cloud",
    request_timeout=120.0,
)

client = chromadb.PersistentClient(path="./chroma_db")
collection = client.get_collection("medcore_rag")

vector_store = ChromaVectorStore(
    chroma_collection=collection
)

index = VectorStoreIndex.from_vector_store(vector_store)

engine = index.as_query_engine(similarity_top_k=5)

questions = [
    "What is the maximum billable quantity for a General Ward Bed?",
    "What is the standard rate for a private room?",
    "What is the patient admission procedure?",
    "What is the employee leave policy?",
    "What are the requirements for patient consent?",
    "What is the procurement approval process?",
    "What is the IT incident response procedure?",
]

print("=" * 70)
print("MEDCORE RAG EVALUATION")
print("=" * 70)

for i, question in enumerate(questions, 1):

    print()
    print(f"TEST {i}")
    print("-" * 70)
    print("QUESTION:", question)

    response = engine.query(question)

    print("ANSWER:", response)

    print("SOURCES:")

    seen = set()

    for source in response.source_nodes:

        metadata = source.node.metadata

        key = (
            metadata.get("department"),
            metadata.get("file_name"),
        )

        if key not in seen:
            seen.add(key)

            print(
                f"  - {metadata.get('department')} | "
                f"{metadata.get('file_name')}"
            )

print()
print("=" * 70)
print("EVALUATION COMPLETE")
print("=" * 70)
