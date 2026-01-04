import faiss
import numpy as np
import json
import os
from sentence_transformers import SentenceTransformer

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

INDEX_PATH = os.path.join(BASE_DIR,'vector_store','faiss.index')

META_PATH = os.path.join(BASE_DIR,'embeddings','embeddings','metadata.json')

model = SentenceTransformer('sentence-transformers/all-MiniLM-L6-v2')

index = faiss.read_index(INDEX_PATH)

with open(META_PATH,'r',encoding='utf-8') as f:
    metadata = json.load(f)
    
def search(query,top_k=5):
    q_emb = model.encode(
        query,
        normalize_embeddings= True,
        
        

    ).astype('float32')
    
    scores,indices = index.search(q_emb.reshape(1,-1),top_k)
    
    results = []
    for i,score in zip(indices[0],scores[0]):
        results.append({
            'score' :float(score),
            'meta':metadata[i]
        })
        
    return results


if __name__ == "__main__":
    results = search('What is artificial intelligence',top_k=5)
    for r in results:
        print(r)