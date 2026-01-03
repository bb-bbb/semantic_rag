import re
import json
import os
from tqdm import tqdm
import tiktoken

RAW_DIR = '../data/raw'
OUT_DIR = '../data/processed'
os.makedirs(OUT_DIR,exist_ok=True)

OUT_FILE = os.path.join(OUT_DIR,'chunks.jsonl')

#토크나이저(openai계열)
tokenizer = tiktoken.get_encoding('cl100k_base')

CHUNK_SIZE =512
OVERLAP = 64


def clean_wiki_text(text:str) ->str:
    stop_patterns=[
        r"\n==\s*References\s*==.*",
        r"\n==\s*External links\s*==.*",
        r"\n==\s*See also\s*==.*",
        r"\n==\s*Further reading\s*==.*",
        r"\nReferences\s*\n.*",
        r"\nExternal links\s*\n.*",
        
    ]
    
    for pattern in stop_patterns:
        text = re.sub(pattern,"",text,flags=re.DOTALL | re.IGNORECASE)
        
    # 과도한 공백정리
    text = re.sub(f"\n{2,}","\n\n",text)
    return text.strip()


def chunk_text(text:str):
    tokens = tokenizer.encode(text) # 문자열토큰화 -> 정수 ID의 리스트 반환
    chunks = []
    
    start=0
    chunk_id = 0
    
    while start < len(tokens):
        end = start + CHUNK_SIZE
        chunk_tokens = tokens[start:end]
        
        # chunk_text = tokenizer.encode(chunk_tokens)
        chunk_text = tokenizer.decode(chunk_tokens)
        
        chunks.append({
            'chunk_id':chunk_id,
            'text':chunk_text
            
        })
        
        chunk_id += 1
        start += CHUNK_SIZE - OVERLAP
    return chunks

def process_documents():
    with open(OUT_FILE, "w", encoding="utf-8") as out_f:
        for filename in tqdm(os.listdir(RAW_DIR)):
            if not filename.endswith(".txt"):
                continue

            doc_id = filename.replace(".txt", "")
            path = os.path.join(RAW_DIR, filename)

            with open(path, "r", encoding="utf-8") as f:
                raw_text = f.read()

            cleaned_text = clean_wiki_text(raw_text)
            chunks = chunk_text(cleaned_text)

            for chunk in chunks:
                record = {
                    "doc_id": doc_id,
                    "chunk_id": chunk["chunk_id"],
                    "source": "wikipedia",
                    "chunk_size": CHUNK_SIZE,
                    "overlap": OVERLAP,
                    "text": chunk["text"]
                }

                out_f.write(json.dumps(record, ensure_ascii=False) + "\n")



if __name__ == "__main__":
    process_documents()
    print("✅ Chunking complete. Saved to data/processed/chunks.jsonl")