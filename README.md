# LangChain-RAG-Summarizer

Retrieval-Augmented Generation (RAG) pipeline for context-aware text summarization and Q&A using LangChain, Ollama, and SQuAD data.

---

**Note:**  
Parts of this project are temporarily non-operational due to a loss of code.  
I am working on re-implementing the missing pieces, and real functionality will be added back soon.

---


## Data

This project uses the [SQuAD dataset](https://rajpurkar.github.io/SQuAD-explorer/) for training and evaluation.

- **train-v2.0.json**: Full training set (about 40MB), _not included in this repo due to size and licensing_
- **dev-v2.0.json**: Official dev/validation set (about 4MB), _not included_
- **sample_squad.json**: Tiny demo sample provided in `data/` for basic testing and repository demonstration

**To run the project on the full dataset:**
1. Download `train-v2.0.json` and `dev-v2.0.json` from [the SQuAD official website](https://rajpurkar.github.io/SQuAD-explorer/)
2. Save both files in your local `data/` directory — they will **not** be uploaded to GitHub.


## Features

- RAG pipeline structure for summarization and QA
- Modular, extendable code organization
- Planned integration for LangChain and Ollama
- Example usage with SQuAD-format data
- Python API using Flask
- Dockerfile for deployment


## Folder Structure

- `/src` — Source code for pipeline modules, API
- `/data` — Example SQuAD-format dataset
- `requirements.txt` — Python dependencies (minimal)
- `Dockerfile` — Container setup for deployment


## Quick Start

1. Clone this repo
2. Install dependencies: `pip install -r requirements.txt`
3. Run the pipeline: `python src/main.py`
4. Try the API: `python src/api.py`


## Current Status

This codebase was originally completed for a Spring 2025 research project;  
however, due to a drive failure, key implementation modules are temporarily unavailable.  
I am actively working on re-implementing core logic for LangChain and Ollama integration.  
Updates will be committed regularly as modules are recovered or rebuilt.

---

## TODO

- Re-implement ML/NLP core functionality
- Restore LangChain & Ollama integration
- Add additional evaluation and improvements as time allows