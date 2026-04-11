rag-project/
│
├── src/
│   ├── main.py                # Entry point (CLI or API)
│   │
│   ├── ingestion/
│   │   ├── loader.py         # Load PDFs / text
│   │   ├── chunker.py        # Fixed-size chunking
│   │
│   ├── embeddings/
│   │   ├── embedder.py       # Create embeddings
│   │
│   ├── retrieval/
│   │   ├── vector_store.py   # FAISS index
│   │   ├── retriever.py      # Query → top-k chunks
│   │
│   ├── generation/
│   │   ├── generator.py      # LLM call
│   │
│   ├── pipeline/
│   │   ├── rag_pipeline.py   # Orchestration logic
│
├── data/
│   ├── raw/                  # PDFs, text files
│   ├── processed/            # Chunked text (optional)
│   ├── vector_store/         # FAISS index files
│
├── config/
│   ├── settings.py           # Constants (chunk size, top_k)
│
├── tests/                    # (empty for now)
│
├── requirements.txt
├── README.md
└── .env

# Note: this was done using ChatGPT, which is why the code is so clean and well-structured.
# Version: 1.0