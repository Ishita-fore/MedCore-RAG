from pathlib import Path

DATA_DIR = Path("data/processed")

files = list(DATA_DIR.rglob("*.md"))

print(f"Found {len(files)} Markdown files")

for file in files:
    print(file)
