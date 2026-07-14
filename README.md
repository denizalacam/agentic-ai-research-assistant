# Agentic AI Research Assistant

> 🚀 **Current Release: Version 2.0**
>
> Agentic AI Research Assistant is a modular AI research platform that combines **Large Language Models (LLMs), Retrieval-Augmented Generation (RAG), web search, PubMed integration, and agentic AI workflows** to automate scientific research tasks.
>
> Version 2 introduces end-to-end biomedical research workflows, including automated literature retrieval, multi-paper scientific synthesis, structured literature review generation, and the initial migration to LangGraph for workflow orchestration.

---

# Version 2 Highlights

### New in Version 2

- ✅ Intelligent planner-based tool selection
- ✅ Local document search (RAG)
- ✅ Real-time web search
- ✅ PubMed integration
- ✅ Automatic PubMed query generation
- ✅ Configurable number of retrieved papers
- ✅ Multi-paper scientific synthesis
- ✅ Automated literature review generation
- ✅ Initial LangGraph workflow orchestration
- ✅ Modular architecture for future expansion

---

# Example Workflow

## Example Workflow

```text
                              User Question
                                     │
                                     ▼
                              Planner Agent
                                     │
                                     ▼
                          Select Appropriate Workflow
                                     │
        ┌──────────────┬─────────────┼─────────────┬──────────────┐
        │              │             │             │              │
        ▼              ▼             ▼             ▼              ▼
   Calculator     Local Search   Web Search   PubMed Search   General LLM
                       │             │             │
                       │             │             ▼
                       │             │       Retrieve Papers
                       │             │             │
                       │             │             ▼
                       │             │      Scientific Synthesis
                       │             │
                       └─────────────┴─────────────┬──────────────┘
                                                 │
                                                 ▼
                                          Final Response
```

For literature-review requests, the PubMed branch continues through an additional generation step:

```text
User Request
     │
     ▼
Planner Agent
     │
     ▼
Literature Review Workflow
     │
     ▼
Generate PubMed Query
     │
     ▼
Retrieve Requested Number of Papers
     │
     ▼
Analyze Titles and Abstracts
     │
     ▼
Synthesize Themes, Methods, Datasets, and Limitations
     │
     ▼
Generate Structured Literature Review
     │
     ▼
Final Response
```

---

# Example

### User Question

```
Write a literature review using 15 recent PubMed papers about multimodal AI for Alzheimer's disease.
```

### The assistant automatically

- Chooses the PubMed workflow
- Generates an optimized PubMed query
- Retrieves the requested number of recent papers
- Reads titles and abstracts
- Synthesizes findings across multiple studies
- Produces a structured literature review
- Includes references using PubMed IDs (PMIDs)

---

# Features

## Intelligent Planner

The assistant automatically determines the best workflow for each user request.

Supported workflows include

- Calculator
- Local Document Search (RAG)
- Web Search
- PubMed Search
- Literature Review Generation
- General LLM Reasoning

---

## Local Document Search (RAG)

Searches user-provided documents to answer questions grounded in local knowledge.

Example

```
What do my notes say about Retrieval-Augmented Generation?
```

---

## Web Search

Retrieves current information for topics requiring up-to-date knowledge.

Example

```
What are the latest generative AI applications in healthcare?
```

---

## PubMed Search

Automatically converts natural language questions into optimized PubMed searches.

Retrieves

- Titles
- Journals
- Publication Years
- PMIDs
- Abstracts

Supports configurable retrieval counts.

Example

```
Find 20 recent PubMed papers about Alzheimer's disease and transformer models.
```

---

## Literature Review Generation

Automatically generates structured literature reviews directly from retrieved PubMed papers.

Generated sections include

- Introduction
- Recent Advances
- Common Methods
- Datasets and Modalities
- Limitations
- Future Directions
- References (PMIDs)

---

# Project Architecture

```
agentic-ai-research-assistant/

├── agents/
│   ├── reasoning_agent.py
│   └── research_agent.py
│
├── graph/
│   ├── state.py
│   ├── nodes.py
│   └── workflow.py
│
├── tools/
│   ├── calculator.py
│   ├── document_search.py
│   ├── pubmed_search.py
│   ├── web_search_tool.py
│   └── tool_types.py
│
├── documents/
├── tests/
│
├── app.py
├── config.py
├── requirements.txt
└── README.md
```

---

# Technologies

- Python
- OpenAI Responses API
- LangGraph
- Agentic AI
- Retrieval-Augmented Generation (RAG)
- PubMed E-Utilities API
- DuckDuckGo Search
- Prompt Engineering
- Object-Oriented Programming
- Modular Software Architecture

---

# Installation

Clone the repository

```bash
git clone https://github.com/denizalacam/agentic-ai-research-assistant.git

cd agentic-ai-research-assistant
```

Install dependencies

```bash
pip install -r requirements.txt
```

Create a `.env` file

```
OPENAI_API_KEY=your_api_key_here
```

Run the assistant

```bash
python app.py
```

---

# Example Questions

```
What is 15% of 280?
```

```
What do my local documents say about Retrieval-Augmented Generation?
```

```
What are the latest generative AI applications in healthcare?
```

```
Find 10 recent PubMed papers about Alzheimer's disease.
```

```
Find 25 recent PubMed papers about multimodal foundation models.
```

```
Write a literature review using 15 recent PubMed papers about multimodal AI for Alzheimer's disease.
```

---

# Release History

## 🚀 Version 2.0 (Current)

### Added

- Planner-based tool selection
- Local RAG
- Web Search
- PubMed Search
- Automatic PubMed query generation
- Configurable paper retrieval
- Multi-paper scientific synthesis
- Literature review generation
- Initial LangGraph integration
- Modular workflow architecture

---

## Version 1.0

### Added

- ResearchAgent
- ReasoningAgent
- Calculator
- Local document search
- Basic Retrieval-Augmented Generation (RAG)
- OpenAI Responses API integration

---

# Roadmap

## Version 3

- Complete LangGraph orchestration
- Parallel workflow execution
- Multi-step research pipelines
- Improved workflow state management

## Version 4

- PDF ingestion
- ChromaDB integration
- Embedding-based semantic search
- Conversation memory
- Citation export
- Markdown export
- PDF export


---

# Author

**Deniz Alacam**


---

# License

This project is released under the MIT License.