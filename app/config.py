import os
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent

MODEL_PATH = os.path.join(BASE_DIR, "models", "mistral-7b-instruct-v0.1.Q5_K_M.gguf")
DATA_PATH = os.path.join(BASE_DIR, "data", "data.xlsx")
INDEX_PATH = os.path.join(BASE_DIR, "index", "faiss_index.bin")
EMBEDDING_PATH = os.path.join(BASE_DIR, "index", "question_embeddings.npy")
EMBEDDING_MODEL = "sentence-transformers/paraphrase-multilingual-MiniLM-L12-v2"

os.makedirs(os.path.dirname(DATA_PATH), exist_ok=True)
os.makedirs(os.path.dirname(INDEX_PATH), exist_ok=True)
os.makedirs(os.path.dirname(MODEL_PATH), exist_ok=True)