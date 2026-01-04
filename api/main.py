from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
import os

from fastapi import FastAPI
from pydantic import BaseModel
from typing import List

from retrieval.retrieve import retrieve
from reranker.reranker import rerank
from retrieval.build_context import build_context
from generation.answer import generate_answer


app = FastAPI(
    title = "Semantic RAG API",
    description='Retrieval-Augmented Generation with FAISS + Claude',
    version = '1.0.0'
    
    
)

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

app.mount(
    "/static",
    StaticFiles(directory=os.path.join(BASE_DIR,'frontend')),
    name='static'
    
)

@app.get("/",response_class =HTMLResponse)
def home():
    with open(os.path.join(BASE_DIR,'frontend','index.html'),encoding='utf-8') as f:
        return f.read()


class AskRequest(BaseModel):
    query:str
    top_k : int=5
    
class Source(BaseModel):
    doc_id:str
    chunk_id : int
    score : float
    source:str
    
class AskResponse(BaseModel):
    query:str
    answer:str
    sources:List[Source]
    
    
@ app.post("/ask",response_model = AskResponse)
def ask(request:AskRequest):
    """
    End-to-End RAG pipeline
    """
    
    #retrieval
    retrieved_chunks= retrieve(
        query = request.query,
        top_k=request.top_k
    )
    
    #rerank
    reranked_chunks = rerank(
        query = request.query,
        retrieved_chunks=retrieved_chunks
        
    )
    
    #context구성
    context = build_context(reranked_chunks)
    
    #answer
    answer = generate_answer(
        query = request.query,
        context=context
        
    )
    
    # source정리
    sources = []
    for chunk in reranked_chunks:
        sources.append(Source(
            doc_id=chunk["doc_id"],
            chunk_id=chunk['chunk_id'],
            score=chunk['score'],
            source=chunk['source']
            
        ))
        
    return AskResponse(
        query=request.query,
        answer=answer,
        sources=sources
        
    )