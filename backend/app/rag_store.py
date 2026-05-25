import faiss
from sentence_transformers import SentenceTransformer
import numpy as np
import pickle
import os

# Initialize embedding model
embed_model = SentenceTransformer("all-MiniLM-L6-v2")

# FAISS index
dim = 384  # embedding dimension of MiniLM
index = faiss.IndexFlatL2(dim)  # L2 distance
metadata_store = []  # store metadata for each vector

# Save/load helper
INDEX_FILE = "rag_index.faiss"
META_FILE = "rag_meta.pkl"

def add_to_index(text: str, source: str):
    """
    Add text + source to FAISS index
    """
    embedding = embed_model.encode([text])
    index.add(np.array(embedding, dtype=np.float32))
    metadata_store.append({"text": text, "source": source})
    save_index()

def add_long_term_memory(text: str):
    add_to_index(text, source="long_term")
    
def search_index(query: str, k=3):
    """
    Search top k relevant items from FAISS
    """
    if index.ntotal == 0:
        return []
    query_embedding = embed_model.encode([query])
    D, I = index.search(np.array(query_embedding, dtype=np.float32), k)
    results = []
    for i in I[0]:
        if i < len(metadata_store):
            results.append(metadata_store[i])
    return results

def save_index():
    faiss.write_index(index, INDEX_FILE)
    with open(META_FILE, "wb") as f:
        pickle.dump(metadata_store, f)

def load_index():
    global index, metadata_store
    if os.path.exists(INDEX_FILE) and os.path.exists(META_FILE):
        index = faiss.read_index(INDEX_FILE)
        with open(META_FILE, "rb") as f:
            metadata_store = pickle.load(f)

# Load index on startup
load_index()

