import faiss
import json
import os
import numpy as np
from sentence_transformers import SentenceTransformer

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

INDEX_PATH = os.path.join(BASE_DIR,'vector_store','faiss.index')
META_PATH = os.path.join(BASE_DIR,'embeddings','embeddings','metadata.json')
CHUNK_PATH = os.path.join(BASE_DIR,'data','processed','chunks.jsonl')


model = SentenceTransformer("sentence-transformers/all-MiniLM-L6-v2")

index = faiss.read_index(INDEX_PATH)
with open(META_PATH,'r',encoding='utf-8') as f:
    metadata = json.load(f)
    
chunk_text_map = {}
with open(CHUNK_PATH,'r',encoding='utf-8') as f:
    for line in f:
        record = json.loads(line)
        chunk_text_map[record['chunk_id']] = record['text']
        
        
def retrieve(query:str, top_k:int = 5):
    """
    Semantic Retrieval
    - input: user query
    - output: top-k relevant chunks
    """
    query_emb = model.encode(
        query,
        normalize_embeddings=True
    ).astype('float32')
    
    scores,indices = index.search(
        query_emb.reshape(1,-1),
        top_k
    )
    
    results = []
    for rank, (idx,score) in enumerate(zip(indices[0],scores[0])):
        meta = metadata[idx]
        chunk_id = meta['chunk_id']
    
        results.append({
            "rank": rank + 1,
            "score": float(score),
            "doc_id" : meta["doc_id"],
            "chunk_id":chunk_id,
            "source": meta['source'],
            'text' : chunk_text_map.get(chunk_id,"")
            
            
        })
    
    return results

if __name__ == "__main__":
    query = "what is artificial intelligence?"
    results = retrieve(query,top_k=5)
    
    for r in results:
        print(f"Rank {r['rank']} | Score {r['score']:.4f}"
              )
        print(r['text'][:300])