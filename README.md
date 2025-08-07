# Persian Q&A System for Call Centers | AI Assistant

**Enterprise-grade FAQ system** combining semantic search with Mistral-7B answer generation, optimized for Persian language support.

## Key Features
- **Hybrid Architecture**: Retrieval-Augmented Generation (RAG) pipeline
- **Language Specialization**: 
  - Persian text normalization (ي/ی, ك/ک, tashkeel removal)
  - Arabic script compatibility
- **Performance Optimizations**:
  - FAISS indexing for 10ms query latency
  - 4-bit quantized Mistral-7B (3.5GB VRAM usage)

## 🛠️ Technical Deep Dive
### Retrieval Engine
```python
# Multilingual Embedding + FAISS
retriever = QARetriever(
    embedding_model="paraphrase-multilingual-MiniLM-L12-v2",
    index_type="FlatIP"  # Inner Product search
)

##  Installation
```bash
git clone https://github.com/yourusername/Q&A-Farsi.git
cd Q&A-Farsi
pip install -r requirements.txt
