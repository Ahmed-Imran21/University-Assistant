# University Assistant using LangGraph and Retrieval-Augmented Generation (RAG)

## Project Overview

The **University Assistant** is an intelligent AI-powered chatbot designed to help students quickly access university-related information. The assistant combines **LangGraph**, **Retrieval-Augmented Generation (RAG)**, **Large Language Models (LLMs)**, and a simple **memory system** to provide accurate, context-aware responses.

Unlike a traditional chatbot, the assistant retrieves information directly from university policy documents before generating an answer, ensuring that responses are grounded in official university documentation rather than relying solely on the LLM's internal knowledge.

The system also supports memory operations, human approval for sensitive responses, and clarification when user queries are ambiguous.

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
| LangGraph | Workflow orchestration |
| LangChain | LLM Framework |
| Groq API | Large Language Model |
| Llama 3.3 70B | Language Model |
| FAISS | Vector Database |
| FastEmbed | Embedding Model |
| Markdown | Knowledge Base |
| dotenv | Environment Variables |

---

# Project Structure

```
UNI-ASSISTANT/
│
├── .env
├── README.md
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

The assistant welcomes the user and introduces its capabilities.

---

## 2. Intent Classification

The user's query is classified into one of the following categories:

- Greeting
- RAG Query
- Memory Request
- Unknown Query

---

## 3. Greeting

Simple greetings receive an immediate conversational response.

---

## 4. Memory

The assistant can

- remember information
- recall previously saved information

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

Instead of searching every document, an LLM first selects the university documents most relevant to the user's question.

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

- loaded
- split into chunks
- embedded using FastEmbed
- indexed with FAISS
- searched using semantic similarity

Only the retrieved document chunks are provided to the language model.

---

## 7. Answer Generation

The LLM generates a response using only the retrieved document context.

The assistant does not invent information beyond the supplied documents.

Each answer includes the source document(s).

---

## 8. Human Review

Certain responses require human approval.

Examples include:

- questions requesting permission
- personal academic decisions
- low-confidence retrieval
- missing information

The reviewer can:

- approve
- edit
- reject

the generated response before it is shown to the user.

---

## 9. Clarification

If the assistant cannot determine the user's intent or retrieve sufficient information, it requests clarification instead of guessing.

---

# Memory System

The assistant maintains a lightweight memory stored in:

```
memory.json
```

Unlike previous implementations, new memories are appended instead of overwriting existing ones.

---

# Retrieval Pipeline

The retrieval pipeline consists of:

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
Embeddings
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
LLM
      │
      ▼
Answer
```

---

# Running the Project

## 1. Clone the repository

```bash
git clone <repository-url>
```

---

## 2. Install dependencies

```bash
pip install -r requirements.txt
```

or

```bash
py -m pip install \
langgraph \
langchain \
langchain-core \
langchain-community \
langchain-groq \
langchain-text-splitters \
langchain-huggingface \
faiss-cpu \
fastembed \
sentence-transformers \
python-dotenv
```

---

## 3. Create a `.env` file

```
GROQ_API_KEY=your_groq_api_key_here
```

---

## 4. Run

```bash
py main.py
```

---

# Example Queries

Greeting

```
Hello
```

---

Policy Question

```
What is the attendance policy?
```

---

Calendar

```
When are final exams?
```

---

Memory

```
Remember I am a Computer Science student.
```

---

Recall Memory

```
What do you remember about me?
```

---

Hostel

```
Can first-year students live off campus?
```

---

Laboratory

```
What happens if I damage lab equipment?
```

---

Unknown Query

```
asdfghjkl
```

---

# Future Improvements

- Persistent FAISS vector database
- Conversation memory using LangGraph Memory
- Multi-turn conversations
- Web interface (Streamlit or Gradio)
- Authentication
- Database-backed memory
- Hybrid retrieval
- Confidence scoring
- Multi-document reasoning
- PDF support
- Administrative dashboard

---

# Author

**Muhammad Imran**

University AI Assistant Project

Built using **Python**, **LangGraph**, **LangChain**, **Groq**, and **Retrieval-Augmented Generation (RAG)**.
