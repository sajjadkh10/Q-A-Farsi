import faiss
import numpy as np
import pandas as pd
from sentence_transformers import SentenceTransformer
from app.config import *
from app.utils import normalize_persian


class QARetriever:
    def __init__(self):
        try:
            self.model = SentenceTransformer(EMBEDDING_MODEL)
            self.index = faiss.read_index(INDEX_PATH)
            self.data = pd.read_excel(DATA_PATH, engine='openpyxl')
            self.embeddings = np.load(EMBEDDING_PATH)
            print("Retriever initialized successfully!")
        except Exception as e:
            raise RuntimeError(f"Failed to initialize retriever: {str(e)}")

    def query(self, question, top_k=3):
        try:
            q_norm = normalize_persian(question)
            q_emb = self.model.encode([q_norm])
            scores, idxs = self.index.search(q_emb, top_k)

            results = []
            for score, idx in zip(scores[0], idxs[0]):
                if idx >= len(self.data):
                    continue

                results.append({
                    "score": float(score),
                    "question": self.data.iloc[idx]["Q"],
                    "answer": self.data.iloc[idx]["A"]
                })
            return results
        except Exception as e:
            print(f"Error in query: {str(e)}")
            return []