from llama_index.embeddings.huggingface import HuggingFaceEmbedding

print("Loading embedding model...")

embed_model = HuggingFaceEmbedding(
    model_name="BAAI/bge-small-en-v1.5"
)

text = "What is the patient admission procedure?"

embedding = embed_model.get_text_embedding(text)

print("Embedding created successfully!")
print("Vector length:", len(embedding))
print("First 10 values:", embedding[:10])
