import wikipediaapi
from tqdm import tqdm
import os,re

# 저장경로
SAVE_DIR = 'data/raw'
os.makedirs(SAVE_DIR,exist_ok=True)

# WikiPedia설정
wiki=wikipediaapi.Wikipedia(
    language='en',
    extract_format = wikipediaapi.ExtractFormat.WIKI,
    user_agent='semantic_rag'
)

CATEGORY_NAME = 'Category:Artificial intelligence'

def collect_category(category_name,max_docs=200):
    category = wiki.page(category_name)
    docs = []
    
    for title,page in category.categorymembers.items():
        if page.ns == wikipediaapi.Namespace.MAIN:
            docs.append(page)
            
        if len(docs) >= max_docs:
            break
        
    
    return docs

def save_documents(pages):
    for page in tqdm(pages):
        text = page.text.strip()
        
        if len(text) < 500: #너무 짧은 문서 제거
            continue
        
        
        filename = re.sub(r'[\\/:*?"<>|]', '_', page.title)
        path = os.path.join(SAVE_DIR,f"{filename}.txt")
        
        with open(path,'w',encoding='utf-8') as f:
            f.write(text)
    
            
if __name__ == "__main__":
    pages = collect_category(CATEGORY_NAME , max_docs=300)
    save_documents(pages)
    # save_documents(pages[130:])   # 130번째 이후부터 이어서 저장

    print(f"saved {len(os.listdir(SAVE_DIR))} documents")


