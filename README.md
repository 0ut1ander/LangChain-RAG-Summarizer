# LangChain-RAG-Summarizer

Retrieval-Augmented Generation (RAG) pipeline for context-aware text summarization and Q&A using LangChain, Ollama, and SQuAD data.

---

## New Demo (Updated Oct. 2025)
*Functional Prototype for Rapid Deployment*

This section represents the current operational logic, developed to showcase a functional RAG workflow using modern LangChain components.

**[ Access the Functional Colab Demo](https://colab.research.google.com/drive/1qFhc_Hs9K-UlUxb5zXp7wyz66RcdzG0X)**

### Demo Architecture:
* **Workflow:** Implements `RecursiveCharacterTextSplitter` for chunking, **ChromaDB** for vector storage, and `RunnablePassthrough` for the final RAG chain.
* **Dual-LLM Strategy:** * **Local Execution:** Uses `flan-t5-small` via HuggingFace for a zero-cost, private, and deterministic environment.
    * **Enterprise Scaling:** Includes a pre-configured template for **UM-GPT (GPT-4o)** integration, ready for high-reasoning research tasks.
* **Key Value:** Demonstrates the ability to build a verifiable, local-first AI tool that can be swapped for powerful APIs in seconds.

---

##  Production Scaling & Architecture
*Optimizing for Large-Scale Research (GB+ Datasets)*

During development, I optimized the architecture to handle common "Big Data" hurdles discussed in research environments:

* **Large-Scale Data Ingestion:** To handle gigabytes of data, I shift from in-memory processing to a **distributed ETL pipeline** using specialized loaders (e.g., PySpark or LangChain’s `DirectoryLoader` with multithreading) to prevent OOM (Out of Memory) errors on standard 16GB RAM hardware.
* **Vector Database Optimization:** For large datasets, I move from local Chroma instances to **managed vector stores (e.g., Pinecone or Milvus)** utilizing **HNSW indexing** for sub-second retrieval across millions of embeddings.
* **Cost Management (Hybrid Routing):** * **Local LLMs (Ollama/Llama 3):** Used for routine summarization or PII-sensitive data to keep costs at zero and maintain data security.
    * **Tiered API Usage:** Reserved for complex reasoning tasks, utilizing smaller models (GPT-4o-mini) for initial processing to reduce token overhead.
* **Containerization:** The included **Dockerfile** ensures that the entire environment—from dependencies to model configurations—is reproducible, meeting ISR’s longitudinal research standards.

---

## Old Project (Spring 2025)
*Legacy Research Evaluation (SQuAD v2.0)*

This codebase served as the foundation for a deep dive into NLP performance using the Stanford Question Answering Dataset.

* **Data Scope:** Evaluated on the full **SQuAD v2.0** (approx. 40MB/100k+ questions).
* **Reproduction:** Focused on **Dockerfile** and **CI/CD via GitHub Actions** to ensure results could be verified by other researchers.
* **Current Status:** Following a hardware failure that impacted key implementation modules, I am actively migrating these legacy research components into the modernized architecture shown in the "New Demo" above.

---

## Folder Structure
* `/src`: Source code for pipeline modules and API.
* `/data`: Contains `sample_squad.json` for repository demonstration.
* `requirements.txt`: Python dependencies.
* `Dockerfile`: Container setup for deployment.

---

## Quick Start
1. **Local Install:** `pip install -r requirements.txt`
2. **Run Demo Logic:** Refer to the [Colab Link](https://colab.research.google.com/drive/1qFhc_Hs9K-UlUxb5zXp7wyz66RcdzG0X).
3. **Docker Build:**
   ```bash
   docker build -t rag-summarizer .
   docker run -p 5000:5000 rag-summarizer

---

## TODO / Roadmap

* Re-implement core ML/NLP functionality into the main Python package.

* Restore native Ollama integration for local-only server deployments.

* Integrate automated evaluation metrics (ROUGE/BLEU) for summarization quality.


