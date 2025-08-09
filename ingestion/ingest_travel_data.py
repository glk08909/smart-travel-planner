# ingestion/ingest_travel_data.py
from datasets import load_dataset
import pandas as pd
from sentence_transformers import SentenceTransformer
import faiss
import numpy as np
import os

# Load dataset
print("Loading dataset...")
#dataset = load_dataset("osunlp/TravelPlanner", split="test")
# ...existing code...
# dataset = load_dataset("osunlp/TravelPlanner", "test")
# # ...existing code...
# df = dataset.to_pandas()

# ...existing code...
dataset = load_dataset("osunlp/TravelPlanner", "test")
df = dataset["test"].to_pandas()
# ...existing code...

# Preview structure
print("Sample record:")
print(df.head(1))

# Extract relevant fields
print("Extracting travel data...")
#df["text"] = df.apply(lambda row: f"Destination: {row['destination']}\nPreferences: {row['preferences']}\nConstraints: {row['constraints']}", axis=1)

# ...existing code...
df["text"] = df.apply(
    lambda row: f"Origin: {row['org']}\nDestination: {row['dest']}\nLevel: {row['level']}\nReference: {row['reference_information']}",
    axis=1
)
# ...existing code...
print(df.columns)

# Save raw text for reference
os.makedirs("data", exist_ok=True)
df[["text"]].to_csv("data/travelplanner_cleaned.csv", index=False)

# Load embedding model
print("Generating embeddings...")
model = SentenceTransformer("all-MiniLM-L6-v2")
embeddings = model.encode(df["text"].tolist(), show_progress_bar=True)

# Save embeddings to FAISS index
print("Saving to FAISS index...")
dimension = embeddings.shape[1]
index = faiss.IndexFlatL2(dimension)
index.add(np.array(embeddings))

faiss.write_index(index, "data/travel_index.faiss")
print("Ingestion complete. FAISS index saved.")
