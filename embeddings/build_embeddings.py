from sentence_transformers import SentenceTransformer
import json
import os
import numpy as np
from tqdm import tqdm

MODEL_NAME = "sentence-transformers/all-MiniLM-L6-v2"
INPUT_PATH = "../data/processed/chunks.jsonl"
OUTPUT_PATH = "embeddings/embeddings.npy"
META_PATH = "embeddings/metadata.json"

os.makedirs('embeddings', exist_ok=True)

model = SentenceTransformer(MODEL_NAME)

embeddings = []
metadata = []

with open(INPUT_PATH,'r',encoding="utf-8 ") as f:
    for line in tqdm(f):
        record = json.loads(line)
        text = record['text']
        
        vector = model.encode(text,normalize_embeddings=True)
        embeddings.append(vector)
        metadata.append({
            "doc_id": record["doc_id"],
            "chunk_id": record["chunk_id"],
            "source": record["source"]
        })

embeddings = np.array(embeddings)

np.save(OUTPUT_PATH, embeddings)

with open(META_PATH, "w", encoding="utf-8") as f:
    json.dump(metadata, f, indent=2)

print(f"Saved {len(embeddings)} embeddings")
    
    