# 🧠 AI-Query Tool: Offline RAG-Powered Assistant

The **AI-Query Tool** is an offline assistant built using a Retrieval-Augmented Generation (RAG) pipeline powered by a local Large Language Model (LLM). It enables users to ask questions against a custom knowledge base (e.g., transcripts) and receive accurate, context-aware answers—completely offline.

---

## 🌐 Project Hosting and Model Reference

> 📎 The local model used in this project is hosted on Hugging Face:

- [`CapybaraHermes-2.5-Mistral-7B.Q4_K_M`](https://huggingface.co/TheBloke/CapybaraHermes-2.5-Mistral-7B-GGUF) by **TheBloke**

This project is intended as a flagship demonstration of building **AI tools** using **local models, Langchain, RAG pipelines, and vector databases**, without needing cloud APIs or online LLMs.

---

## 🤖 Brief: Why AI Tools Matter

AI tools—particularly **AI agents** and **agentic systems**—have transformed the way we interact with knowledge, automate tasks, and build scalable, intelligent products. These tools act as intelligent assistants that can retrieve, reason, and respond using natural language.

### 🌍 Real-World Importance

- **💼 Enterprises** use AI agents to automate workflows, enhance customer support, and streamline internal knowledge access.
- **🏥 Healthcare** leverages AI to summarize patient records and assist in diagnosis.
- **⚖️ Legal** professionals use document-augmented tools to summarize laws and contracts.
- **🔐 Cybersecurity** teams use LLMs for code analysis, threat detection, and documentation.
- **🏫 Education** benefits from personalized tutoring and question-answering agents.

> 📊 **Statistically**, a [2023 McKinsey report](https://www.mckinsey.com/) found that companies using LLMs and AI-enhanced tools boosted productivity by **20-30%** in knowledge work domains.

---

## 🧠 Agent vs. Agentic AI

- **AI Agents** are tools designed to perform one or more tasks using language and reasoning, often based on instructions or data.
- **Agentic AI** refers to systems that **autonomously** plan, reason, and execute actions in a goal-directed manner, often involving memory, planning, and environmental interaction.

> 🔍 This project is an **AI Agent** rather than agentic AI. It does not plan or act autonomously, but responds intelligently to human queries using Retrieval-Augmented Generation (RAG).

---

## 🧱 Tech Stack Overview

| Layer            | Tool/Framework                            | Purpose                                            |
| ---------------- | ----------------------------------------- | -------------------------------------------------- |
| **LLM**          | CapybaraHermes / Mistral 7B (GGUF, local) | Local inference for natural language understanding |
| **RAG Engine**   | Langchain                                 | Modular orchestration for retrieval & generation   |
| **Vector DB**    | ChromaDB                                  | Fast local similarity search and retrieval         |
| **Embedding**    | SentenceTransformers (MiniLM)             | Convert chunks and queries into semantic vectors   |
| **Runner**       | Custom Python pipeline                    | Custom orchestration in `rag_pipeline.py`          |
| **Model Loader** | llama-cpp-python                          | Efficient LLM runtime for local inference          |
| **UI / CLI**     | Terminal-based interface                  | Simple user interaction loop                       |

---

## 🏗️ System Architecture

```
                ┌──────────────────────────────┐
                │         User Query           │
                └────────────┬─────────────────┘
                             ▼
               ┌──────────────────────────────┐
               │ SentenceTransformer Embedding│
               └────────────┬─────────────────┘
                             ▼
                ┌────────────────────────────┐
                │      ChromaDB Search       │◄────── Vector DB (local)
                └────────────┬───────────────┘
                             ▼
               ┌──────────────────────────────┐
               │  Retrieved Chunks + Prompt   │
               └────────────┬─────────────────┘
                             ▼
               ┌──────────────────────────────┐
               │     CapybaraHermes LLM       │
               └────────────┬─────────────────┘
                             ▼
                   ┌────────────────────┐
                   │   Final Response   │
                   └────────────────────┘
```

---

## 📦 Setup Instructions

### 1. Create a Python Virtual Environment

```bash
python3 -m venv venv
source venv/bin/activate    # On Windows: venv\Scripts\activate
```

### 2. Install Dependencies

```bash
pip install -r requirements.txt
```

> **M1/M2 Mac Users:**  
> If you face issues with `llama-cpp-python`:

```bash
CMAKE_ARGS="-DLLAMA_METAL=on" FORCE_CMAKE=1 pip install -U llama-cpp-python --no-cache-dir
```

---

## 📂 Folder Structure

```
├── run.py                 # Main entry point to launch the assistant
├── app/                   # RAG pipeline and supporting logic
├── vector_db/             # Local ChromaDB vector storage
├── local_models/          # Contains GGUF format LLMs
├── data/                  # JSON transcripts for embedding
├── requirements.txt       # Dependency list
├── README.md              # Project overview
├── hallucination_report.md # Notes on model inaccuracies
```

---

## 🧠 Local Model: CapybaraHermes-2.5-Mistral-7B.Q4_K_M

**Model:** [`CapybaraHermes-2.5-Mistral-7B`](https://huggingface.co/TheBloke/CapybaraHermes-2.5-Mistral-7B-GGUF)  
**Author:** TheBloke  
**Size:** ~4.37 GB  
**Format:** GGUF

> Also includes **LLaMA 2 7B** (GGUF) in `local_models/` for model comparisons.

---

## 🔍 What is RAG?

**Retrieval-Augmented Generation (RAG)** combines information retrieval with LLMs to deliver accurate, context-aware responses.

### 🧱 Two-Phase Pipeline

1. **Data Preparation:**
   - Chunk documents → Embed into vectors → Store in ChromaDB
2. **Query Time:**
   - Embed user question → Retrieve top matches → Feed into LLM

---

## ▶️ Running the Assistant

```bash
python run.py
```

- Type `exit` or `quit` to end session.
- Use `deactivate` to exit the Python virtual environment.

---

## 🚨 Hallucination Awareness

LLMs may produce **hallucinations**—incorrect or made-up facts. See [`hallucination_report.md`](./hallucination_report.md) for examples and tips to mitigate.

---

## 💡 Use Cases

- Ask questions over large document datasets (e.g., transcripts, legal files)
- Offline Q&A for secure environments
- Developer tools for benchmarking local LLMs

---

## 🔐 Offline, Private, and Powerful

This assistant runs **completely offline**. No API keys, no cloud dependencies, no internet access required.

---

## 🏁 Final Notes

This project serves as a **flagship example** of building performant, offline-capable AI tooling using modern open-source technologies.

If you found this helpful or insightful, give it a ⭐ on GitHub and stay tuned for future updates.
