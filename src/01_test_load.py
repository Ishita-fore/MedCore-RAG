from pathlib import Path
from llama_index.core import Document

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

print("Document loaded successfully!")
print("File:", document.metadata["file_name"])
print("Department:", document.metadata["department"])
print("Characters:", len(document.text))
print()
print(document.text[:1000])
