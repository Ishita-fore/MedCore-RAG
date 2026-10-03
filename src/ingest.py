from pathlib import Path
import re
import chromadb

from llama_index.core import Document, VectorStoreIndex, StorageContext, Settings
from llama_index.embeddings.huggingface import HuggingFaceEmbedding
from llama_index.vector_stores.chroma import ChromaVectorStore


DATA_DIR = Path("data/processed")
CHROMA_DIR = "./chroma_db"
COLLECTION_NAME = "medcore_rag"

print("Loading embedding model...")

Settings.embed_model = HuggingFaceEmbedding(
    model_name="BAAI/bge-small-en-v1.5"
)


def is_table_line(line):
    return line.strip().startswith("|") and line.strip().endswith("|")


def is_separator_line(line):
    if not is_table_line(line):
        return False

    cells = line.strip().strip("|").split("|")
    return all(
        re.fullmatch(r"\s*:?-+:?\s*", cell)
        for cell in cells
    )


def create_chunks(text, max_chars=6000):
    """
    Table-aware Markdown chunker.

    - Keeps Markdown tables together.
    - Keeps the table header with its rows.
    - Splits ordinary prose into reasonably sized chunks.
    """

    lines = text.splitlines()
    chunks = []

    current = []
    current_len = 0
    i = 0

    while i < len(lines):
        line = lines[i]

        # Detect Markdown table
        if (
            i + 1 < len(lines)
            and is_table_line(line)
            and is_separator_line(lines[i + 1])
        ):
            # Save preceding prose
            if current:
                chunk = "\n".join(current).strip()
                if chunk:
                    chunks.append(chunk)
                current = []
                current_len = 0

            # Capture entire table
            table_lines = [line, lines[i + 1]]
            i += 2

            while i < len(lines) and is_table_line(lines[i]):
                table_lines.append(lines[i])
                i += 1

            table_text = "\n".join(table_lines).strip()

            # Keep table intact when reasonably sized.
            # If extremely large, split by rows while repeating header.
            if len(table_text) <= max_chars:
                chunks.append(table_text)
            else:
                header = "\n".join(table_lines[:2])
                rows = table_lines[2:]

                table_chunk = [header]
                table_len = len(header)

                for row in rows:
                    if table_len + len(row) + 1 > max_chars:
                        chunks.append("\n".join(table_chunk))
                        table_chunk = [header, row]
                        table_len = len(header) + len(row)
                    else:
                        table_chunk.append(row)
                        table_len += len(row) + 1

                if len(table_chunk) > 2:
                    chunks.append("\n".join(table_chunk))

            continue

        # Ordinary Markdown/prose
        if line.strip():
            current.append(line)
            current_len += len(line) + 1

            if current_len >= max_chars:
                chunks.append("\n".join(current).strip())
                current = []
                current_len = 0
        else:
            if current:
                current.append("")

        i += 1

    if current:
        chunk = "\n".join(current).strip()
        if chunk:
            chunks.append(chunk)

    return chunks


print("Loading Markdown documents...")

documents = []
markdown_files = sorted(DATA_DIR.rglob("*.md"))

print(f"Found {len(markdown_files)} Markdown files.")

for file_path in markdown_files:
    department = file_path.parent.name
    filename = file_path.name
    lower_name = filename.lower()

    if "policy" in lower_name:
        document_type = "Policy"
    elif "sop" in lower_name:
        document_type = "SOP"
    elif "handbook" in lower_name:
        document_type = "Handbook"
    elif "matrix" in lower_name:
        document_type = "Matrix"
    elif "guide" in lower_name:
        document_type = "Guide"
    elif "checklist" in lower_name:
        document_type = "Checklist"
    else:
        document_type = "Other"

    text = file_path.read_text(encoding="utf-8")

    chunks = create_chunks(text)

    for chunk_number, chunk in enumerate(chunks, start=1):
        documents.append(
            Document(
                text=chunk,
                metadata={
                    "department": department,
                    "file_name": filename,
                    "document_type": document_type,
                    "source": str(file_path),
                    "chunk_number": chunk_number,
                },
            )
        )

print(f"Created {len(documents)} retrieval chunks.")

print("Connecting to Chroma...")

chroma_client = chromadb.PersistentClient(path=CHROMA_DIR)

# Remove old collection so old bad chunks cannot remain.
try:
    chroma_client.delete_collection(COLLECTION_NAME)
    print("Deleted old collection.")
except Exception:
    pass

collection = chroma_client.get_or_create_collection(
    name=COLLECTION_NAME
)

vector_store = ChromaVectorStore(
    chroma_collection=collection
)

storage_context = StorageContext.from_defaults(
    vector_store=vector_store
)

print("Creating vector index...")
print("This may take a few minutes.")

VectorStoreIndex.from_documents(
    documents,
    storage_context=storage_context,
    show_progress=True,
)

print()
print("=" * 60)
print("INGESTION COMPLETE")
print("=" * 60)
print(f"Markdown files: {len(markdown_files)}")
print(f"Retrieval chunks: {len(documents)}")
print(f"Chroma collection: {COLLECTION_NAME}")
print(f"Chroma path: {CHROMA_DIR}")
PY
