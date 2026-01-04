from sentence_transformers import CrossEncoder
from typing import List, Dict

model = CrossEncoder("cross-encoder/ms-marco-MiniLM-L-6-v2")


def rerank(
    query : str,
    retrieved_chunks: List[Dict],
    top_k : int=3
    
):
    """
    Cross-Encoder Reranking
    input:
        query: user query
        retrieved_chunks: retrieval 결과
    output:
        reranked top_k chunks
    """
    
    pairs = [
        (query,chunk['text'])
        for chunk in retrieved_chunks
        
        
    ]
    
    scores = model.predict(pairs)
    
    for chunk, score in zip(retrieved_chunks,scores):
        chunk['rerank_score'] = float(score)
        
    reranked = sorted(
        retrieved_chunks,
        key=lambda x:x['rerank_score'],
        reverse=True
        
        
    )
    return reranked[:top_k]


if __name__ == "__main__":
    retrieved = [
        {"text": "AI is the simulation of human intelligence in machines."},
        {"text": "Artificial intelligence is a branch of computer science."},
        {"text": "AI can be categorized into narrow and general intelligence."}
        
    ]
    
    query = 'What is artificial intelligence?'
    results = rerank(query, retrieved)
    for r in results:
        print(r['rerank_score'],r['text'])