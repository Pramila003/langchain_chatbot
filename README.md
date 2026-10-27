# LangChain RAG Chatbot

A Python project scaffold for experimenting with retrieval-augmented generation (RAG). The current ingestion path loads PDF and text documents, splits them into chunks, creates Sentence Transformer embeddings, and stores them in Qdrant.

> **Project status:** Document ingestion is implemented. The terminal chat entry point and the modules for the RAG chain, prompts, and reusable vector-store access are currently placeholders, so an end-to-end chatbot is not yet available.

## What is currently implemented

- **Document loading:** `src/loaders.py` reads PDF and UTF-8 text files from `data/raw/`.
- **Chunking:** Documents are split into chunks of 800 characters with 200 characters of overlap.
- **Embeddings:** `src/embeddings.py` uses `sentence-transformers/all-MiniLM-L6-v2` with normalized embeddings.
- **Vector storage:** `scripts/ingest.py` sends the chunks to the configured Qdrant collection. The collection name defaults to `deterministic`.
- **Configuration:** `src/config.py` loads settings from environment variables and a local `.env` file.

## Project layout

```text
.
├── data/
│   └── raw/                 # Source documents to ingest (PDF and TXT)
├── scripts/
│   ├── chat.py              # Placeholder for a terminal chat interface
│   └── ingest.py            # Load, split, embed, and store documents
├── src/
│   ├── chains.py            # Placeholder for the RAG/LLM chain
│   ├── config.py            # Environment-based settings
│   ├── embeddings.py        # Hugging Face/Sentence Transformer embeddings
│   ├── loaders.py           # Document loading and text splitting
│   ├── prompts.py           # Placeholder for prompts
│   └── vector_store.py      # Placeholder for reusable Qdrant access
├── tests/
│   ├── test_embeddings.py   # Placeholder for embedding tests
│   ├── test_groq.py         # Manual Groq API smoke test
│   └── test_retrieval.py    # Placeholder for retrieval tests
├── .env.example             # Environment-variable template
└── requirements.txt         # Python dependencies
```

The repository includes `data/raw/cancer_doc.pdf` as an example source document. Add your own supported files under `data/raw/` to ingest them.

## Requirements

- Python
- A Qdrant instance and its URL/API key
- A Groq API key for the Groq smoke test and future chat functionality

The embedding model may be downloaded the first time embeddings are initialized.

## Setup

From the project root, create and activate a virtual environment, then install the dependencies:

```powershell
py -m venv .venv
.\.venv\Scripts\Activate.ps1
python -m pip install -r requirements.txt
python tests/tset_groq.py
python -m scripts.ingest
```


Copy the example environment file and fill in your service credentials:

```powershell
Copy-Item .env.example .env
```

Set these values in `.env`:

```dotenv
GROQ_API_KEY=your_groq_api_key
QDRANT_URL=your_qdrant_url
QDRANT_API_KEY=your_qdrant_api_key
```

Optional settings used by the configuration module:

| Variable | Default | Purpose |
| --- | --- | --- |
| `QDRANT_COLLECTION` | `deterministic` | Qdrant collection name |
| `EMBEDDING_MODEL` | `sentence-transformers/all-MiniLM-L6-v2` | Hugging Face embedding model |

Keep `.env` private; it is excluded from version control.

## Ingest documents

Place PDF or UTF-8 `.txt` files in `data/raw/`, then run:

```powershell
python -m scripts.ingest
```

The script loads and splits documents, writes the resulting vectors to Qdrant, and prints the number of indexed chunks. It requires a working Qdrant endpoint and credentials.

## Chat and tests

`scripts/chat.py`, `src/chains.py`, `src/prompts.py`, and `src/vector_store.py` do not yet contain chatbot functionality.

`tests/test_embeddings.py` and `tests/test_retrieval.py` are placeholders. `tests/test_groq.py` is a standalone smoke test that sends a live request to Groq and prints the response; it requires `GROQ_API_KEY` and may consume API quota. It is not a unit test suite.

## Current limitation

The document loader currently returns from inside its file-scanning loop. As a result, an ingestion run processes only the first supported file it encounters rather than every supported file in `data/raw/`. This should be corrected before relying on ingestion of multiple documents.


