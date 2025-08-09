# retrieval/retriever.py

import os
import faiss
import pandas as pd
import numpy as np
import tiktoken
from sentence_transformers import SentenceTransformer

# Validate file paths
assert os.path.exists("data/travelplanner_cleaned.csv"), "CSV file not found"
assert os.path.exists("data/travel_index.faiss"), "FAISS index not found"

# Load cleaned travel data
df = pd.read_csv("data/travelplanner_cleaned.csv")

# Load FAISS index
index = faiss.read_index("data/travel_index.faiss")

# Load embedding model
model = SentenceTransformer("all-MiniLM-L6-v2")

def retrieve_chunks(query, k=3):
    query_embedding = model.encode([query])
    distances, indices = index.search(np.array(query_embedding), k)
    results = df.iloc[indices[0]]["text"].values.tolist()
    return [chunk[:1000] for chunk in results]  # Limit each chunk to ~1000 characters

import tiktoken

def count_tokens(text, model="gpt-3.5-turbo"):
    enc = tiktoken.encoding_for_model(model)
    return len(enc.encode(text))

# Example usage
if __name__ == "__main__":
    user_query = "Plan a 3-day trip to Tokyo under $1000"
    top_chunks = retrieve_chunks(user_query)
    
    print("\nTop Retrieved Chunks:")
    for i, chunk in enumerate(top_chunks, 1):
        print(f"\n[{i}] {chunk}")
