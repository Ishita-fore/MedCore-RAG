from pathlib import Path

import chromadb

from llama_index.core import (
    Document,
    StorageContext,
    VectorStoreIndex,
    Settings,
)

from llama_index.embeddings.huggingface import HuggingFaceEmbedding
from llama_index.vector_stores.chroma import ChromaVectorStore


# --------------------------------------------------
# 1. Embedding model
# --------------------------------------------------

print("Loading embedding model...")

Settings.embed_model = HuggingFaceEmbedding(
    model_name="BAAI/bge-small-en-v1.5"
)


# --------------------------------------------------
# 2. Read ONE document
# --------------------------------------------------

file_path = Path(
    "data/processed/Clinical_Operations/01_Patient_Admission_SOP.md"
)

text = file_path.read_text(encoding="utf-8")


document = Document(
    text=text,
    metadata={
        "department": "Clinical Operations",
        "file_name": file_path.name,
        "document_type": "SOP",
    },
)


# --------------------------------------------------
# 3. Create persistent Chroma database
# --------------------------------------------------

chroma_client = chromadb.PersistentClient(
    path="./chroma_db"
)

collection = chroma_client.get_or_create_collection(
    name="medcore_test"
)


# --------------------------------------------------
# 4. Connect Chroma to LlamaIndex
# --------------------------------------------------

vector_store = ChromaVectorStore(
    chroma_collection=collection
)

storage_context = StorageContext.from_defaults(
    vector_store=vector_store
)


# --------------------------------------------------
# 5. Create vector index
# --------------------------------------------------

print("Creating vector index...")

index = VectorStoreIndex.from_documents(
    [document],
    storage_context=storage_context,
)


print("SUCCESS!")
print("Document has been embedded and stored in Chroma.")
