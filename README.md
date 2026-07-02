# University Assistant using LangGraph and Retrieval-Augmented Generation (RAG)

## Project Overview

The **University Assistant** is an AI-powered chatbot designed to help students quickly access university-related information. The assistant combines **LangGraph**, **Retrieval-Augmented Generation (RAG)**, **Large Language Models (LLMs)**, and a lightweight **memory system** to provide accurate, context-aware responses.

Unlike a traditional chatbot, the assistant retrieves information directly from university policy documents before generating an answer, ensuring that responses are grounded in official university documentation rather than relying solely on the LLM's internal knowledge.

The assistant also supports memory operations, human approval for sensitive responses, and clarification when user queries are ambiguous.

---

# Features

- Intent Classification using an LLM
- LangGraph-based workflow orchestration
- Retrieval-Augmented Generation (RAG)
- Intelligent Document Picker
- FAISS Vector Database
- FastEmbed Embeddings
- Memory System
- Human Review Workflow
- Clarification for Unknown Queries
- Source Attribution
- Modular Python Architecture

---

# System Architecture

```
                    START
                      │
                      ▼
              Welcome Message
                      │
                      ▼
             Receive User Query
                      │
                      ▼
            Intent Classification
                      │
      ┌───────────────┼────────────────┐
      │               │                │
      ▼               ▼                ▼
 Greeting          Memory          RAG Query
                      │                │
                      │        Document Picker
                      │                │
                      │                ▼
                      │      Retrieve Documents
                      │                │
                      │                ▼
                      │      Generate Answer
                      │                │
                      └──────► Review Decision
                                  │
                  ┌───────────────┴───────────────┐
                  │                               │
                  ▼                               ▼
          Human Review                    Final Answer
                  │
                  ▼
             Final Answer
                  │
                  ▼
                  END
```

---

# Technologies Used

| Technology | Purpose |
|------------|---------|
| Python | Programming Language |
| LangGraph | Workflow Orchestration |
| LangChain | LLM Framework |
| Groq API | LLM Inference |
| Llama 3.3 70B | Large Language Model |
| FAISS | Vector Database |
| FastEmbed | Embedding Model |
| Markdown | Knowledge Base |
| python-dotenv | Environment Variable Management |

---

# Project Structure

```
UNI-ASSISTANT/
│
├── .env
├── .gitignore
├── README.md
├── requirements.txt
│
├── code_pipeline/
│   ├── graph.py
│   ├── human_review.py
│   ├── main.py
│   ├── memory.py
│   ├── memory.json
│   ├── nodes.py
│   ├── rag_pipeline.py
│   └── state.py
│
├── data/
│   ├── academic_calendar.md
│   ├── attendance_policy.md
│   ├── contact_directory.md
│   ├── grading_policy.md
│   ├── hostel_rules.md
│   └── lab_guidelines.md
│
└── project_question/
```

---

# Workflow Description

## 1. Welcome

The assistant greets the user and introduces itself before accepting queries.

---

## 2. Intent Classification

The user's question is classified into one of four categories:

- Greeting
- RAG Query
- Memory Request
- Unknown Query

---

## 3. Greeting

Greeting messages receive a simple conversational response.

---

## 4. Memory

The assistant can store and recall user information.

Example:

```
Remember my favourite subject is AI.
```

Later:

```
What do you remember about me?
```

---

## 5. Document Picker

An LLM determines which university documents are most relevant to the user's question before retrieval begins.

Available documents include:

- Academic Calendar
- Attendance Policy
- Grading Policy
- Hostel Rules
- Laboratory Guidelines
- Contact Directory

---

## 6. Retrieval-Augmented Generation (RAG)

The selected documents are:

- Loaded
- Split into chunks
- Embedded using FastEmbed
- Indexed with FAISS
- Retrieved using semantic similarity search

Only the retrieved document chunks are supplied to the language model.

---

## 7. Answer Generation

The LLM generates an answer using **only** the retrieved document context.

Each answer also includes the document(s) used as sources.

---

## 8. Human Review

Sensitive or uncertain responses are sent for human approval.

Examples include:

- Permission requests
- Personal academic decisions
- Low-confidence retrieval
- Missing information

The reviewer may:

- Approve
- Edit
- Reject

before the answer is returned to the user.

---

## 9. Clarification

If the assistant cannot determine the user's intent or retrieve sufficient information, it asks the user to clarify their question instead of guessing.

---

# Memory System

User memories are stored in:

```
memory.json
```

New memories are appended, ensuring previous information is preserved.

---

# Retrieval Pipeline

```
User Question
      │
      ▼
Document Picker
      │
      ▼
Selected Documents
      │
      ▼
Text Splitter
      │
      ▼
FastEmbed Embeddings
      │
      ▼
FAISS Vector Store
      │
      ▼
Similarity Search
      │
      ▼
Retrieved Chunks
      │
      ▼
Groq LLM
      │
      ▼
Generated Answer
```

---

# Prerequisites

Before running the project, ensure you have:

- Python 3.10 or newer
- A Groq API key
- Internet connection (for Groq API)

---

# Installation

Clone the repository:

```bash
git clone <repository-url>
```

Move into the project directory:

```bash
cd UNI-ASSISTANT
```

Install all required packages:

```bash
py -m pip install -r requirements.txt
```

---

# Environment Variables

Create a file named `.env` in the project root.

Add your Groq API key:

```
GROQ_API_KEY=your_groq_api_key_here
```

---

# Running the Project

Move into the pipeline directory:

```bash
cd code_pipeline
```

Run:

```bash
py main.py
```

---

# Example Queries

### Greeting

```
Hello
```

### Attendance

```
What is the attendance policy?
```

### Academic Calendar

```
When are the final examinations?
```

### Memory

```
Remember I am a Computer Science student.
```

### Recall Memory

```
What do you remember about me?
```

### Hostel

```
Can first-year students live off campus?
```

### Laboratory

```
What happens if I damage laboratory equipment?
```

### Unknown Query

```
asdfghjkl
```

---

# Future Improvements

- Persistent FAISS index
- Multi-turn conversations
- LangGraph Memory integration
- Hybrid Retrieval
- Confidence scoring
- Multi-document reasoning
- PDF and DOCX support
- Streamlit or Gradio web interface
- Authentication system
- Administrative dashboard

---

# Author

**Muhammad Ahmed Imran**

University Assistant Project

Built using **Python**, **LangGraph**, **LangChain**, **Groq**, **FAISS**, and **Retrieval-Augmented Generation (RAG)**.

---

# License

This project was developed for educational purposes as part of a university assignment.
