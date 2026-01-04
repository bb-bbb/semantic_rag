import faiss
import numpy as np
import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

EMB_PATH = os.path.join(BASE_DIR,'embeddings','embeddings','embeddings.npy')
INDEX_PATH = os.path.join(BASE_DIR,'vector_store','faiss.index')

os.makedirs(os.path.dirname(INDEX_PATH),exist_ok = True)

#LOAD embeddings
embeddings = np.load(EMB_PATH).astype('float32')

dim = embeddings.shape[1]

# Cosine similarity = Inner product + normalized vectors
index = faiss.IndexFlatIP(dim)

index.add(embeddings)
faiss.write_index(index,INDEX_PATH)

print(f'FAISS index built with {index.ntotal} vectors')
