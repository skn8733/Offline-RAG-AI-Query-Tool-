# vector_store.py
import os
import json
from langchain.text_splitter import RecursiveCharacterTextSplitter
from sentence_transformers import SentenceTransformer
import chromadb

def load_json_transcripts(folder):
    data = []
    for file in os.listdir(folder):
        if file.endswith(".json"):
            with open(os.path.join(folder, file), "r", encoding="utf-8") as f:
                obj = json.load(f)
                data.append({"filename": obj["filename"], "text": obj["text"]})
    return data

def chunk_transcripts(data):
    splitter = RecursiveCharacterTextSplitter(chunk_size=500, chunk_overlap=100)
    chunks = []
    for entry in data:
        for chunk in splitter.split_text(entry["text"]):
            chunks.append({
                "content": chunk,
                "metadata": {"source": entry["filename"]}
            })
    return chunks

def store_chunks(chunks, persist_dir="./vector_db"):
    model = SentenceTransformer("all-MiniLM-L6-v2")  # Fast, small, accurate
    client = chromadb.PersistentClient(path=persist_dir)
    collection = client.get_or_create_collection("expert_calls")

    for i, chunk in enumerate(chunks):
        embedding = model.encode(chunk["content"]).tolist()
        collection.add(
            documents=[chunk["content"]],
            embeddings=[embedding],
            ids=[f"chunk_{i}"],
            metadatas=[chunk["metadata"]]
        )

    print(f"Stored {len(chunks)} chunks in vector DB at {persist_dir}")

if __name__ == "__main__":
    transcripts = load_json_transcripts("data/transcripts_json")
    chunks = chunk_transcripts(transcripts)
    store_chunks(chunks)
