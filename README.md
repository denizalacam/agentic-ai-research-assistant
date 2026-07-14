# Agentic AI Research Assistant

Agentic AI Research Assistant is a modular AI software system that demonstrates how large language models, reasoning agents, and external tools can be orchestrated to solve research tasks. The project is built with Python and the OpenAI Responses API and is designed to evolve from a simple local RAG system into a production-style multi-agent research platform.

Version 1 focuses on local document retrieval and tool-assisted reasoning. Future versions will expand the system with semantic search, PubMed integration, vector databases, and multi-tool orchestration.

---

## Motivation

Modern AI applications require more than a single LLM call. They often combine reasoning, external tools, retrieval systems, and modular software architecture.

This project explores those concepts by incrementally building an extensible agentic AI research assistant.

---

## Learning Objectives

This project is designed to demonstrate and explore:

- Agentic AI workflows
- Large Language Models (LLMs)
- Retrieval-Augmented Generation (RAG)
- Tool selection and orchestration
- Software architecture for AI applications
- Object-oriented design in Python

---

## Current Capabilities

* OpenAI Responses API integration
* Modular agent architecture
* ReasoningAgent for tool selection
* ResearchAgent for workflow coordination
* Calculator tool
* Local document search
* Basic Retrieval-Augmented Generation (RAG)
* Environment-based configuration using `.env`
* Clean, extensible project structure

---

## Project Architecture

```
                    User
                      │
                      ▼
              ReasoningAgent
                      │
         Chooses the appropriate tool
                      │
        ┌─────────────┴─────────────┐
        ▼                           ▼
 Calculator Tool          Document Search Tool
        │                           │
        └─────────────┬─────────────┘
                      ▼
               ResearchAgent
                      │
                      ▼
               Final Response
```

---

## Technologies

- Python
- OpenAI Responses API
- python-dotenv
- Rich
- Object-Oriented Programming (OOP)
- Retrieval-Augmented Generation (RAG)
- Modular AI Architecture

---

## Project Structure

```
agentic-ai-research-assistant/
│
├── app.py
├── config.py
├── requirements.txt
├── README.md
├── .env.example
├── .gitignore
│
├── agents/
│   ├── reasoning_agent.py
│   └── research_agent.py
│
├── tools/
│   ├── calculator.py
│   ├── document_search.py
│   └── tool_types.py
│
├── documents/
├── screenshots/
└── tests/
```

---

## Installation

Clone the repository:

```bash
git clone https://github.com/<your-username>/agentic-ai-research-assistant.git
cd agentic-ai-research-assistant
```

Create and activate a Conda environment:

```bash
conda create -n agentic-ai python=3.12
conda activate agentic-ai
```

Install the required packages:

```bash
pip install -r requirements.txt
```

Create a `.env` file:

```
OPENAI_API_KEY=your_api_key_here
```

Run the application:

```bash
python app.py
```

---

## Example

**Question**

```
What do my notes say about RAG?
```

**Answer**

```
Retrieval-Augmented Generation (RAG) improves LLM applications by allowing the model to answer questions using external documents instead of relying only on its training data.
```

---

## Project Status

This repository is under active development. Each version introduces additional agentic AI capabilities while preserving a modular architecture.

---

## Current Version (v1.0)

* Local document retrieval
* Calculator tool
* LLM-powered reasoning agent
* Basic RAG workflow
* Modular software architecture

---

## Planned Features

### Version 2

* PubMed integration
* Literature review generation
* Tool executor
* Improved reasoning workflow

### Version 3

* Embeddings
* ChromaDB
* Semantic search
* PDF ingestion

### Version 4

* Multi-tool planning
* Conversation memory
* Streaming responses
* Evaluation framework

---

## Technologies

* Python
* OpenAI Responses API
* python-dotenv
* Rich
* Object-Oriented Programming (OOP)

---

# Author

**Deniz Alacam**


---

# License

This project is released under the MIT License.
