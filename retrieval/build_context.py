def build_context(reranked_chunks):
    blocks = []
    
    for i, chunk in enumerate(reranked_chunks):
        block = f"""[Document {i+1}
Source: {chunk['source']}
DocID: {chunk['doc_id']}
ChunkID: {chunk['chunk_id']}
Score: {chunk.get('rerank_score', chunk.get('score', 0))}]

{chunk['text']}
"""
        blocks.append(block)
        
    return "\n\n".join(blocks)