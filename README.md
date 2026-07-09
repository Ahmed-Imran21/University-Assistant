# 🎓 University Assistant (Streamlit Edition)

An AI-powered University Assistant built using **LangGraph**, **LangChain**, **Retrieval-Augmented Generation (RAG)**, **Groq LLMs**, and **Streamlit**.

This version provides a modern web-based interface for interacting with the assistant. It can answer university-related questions using official university documents, remember user information, and request human approval for sensitive responses.

---

# Features

- 🎓 Interactive Streamlit web interface
- 🤖 LangGraph workflow orchestration
- 🧠 LLM-based intent classification
- 📚 Retrieval-Augmented Generation (RAG)
- 📄 Intelligent document selection
- 🔍 Semantic document retrieval with FAISS
- ⚡ FastEmbed embeddings
- 💾 Persistent memory system
- 👨‍💼 Human review workflow
- ❓ Unknown query clarification
- 📖 Source attribution
- 🧑‍💻 Developer mode
- 📊 Retrieval statistics

---

# System Architecture

```
                    START
                      │
                      ▼
              Welcome Screen
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
        Human Review (UI)                 Final Answer
                  │
                  ▼
                  END
```

---

# Technologies Used

| Technology | Purpose |
|------------|---------|
| Python | Programming Language |
| Streamlit | Web Interface |
| LangGraph | Workflow Orchestration |
| LangChain | AI Framework |
| Groq API | LLM Provider |
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
├── requirements.txt
├── streamlit_app.py
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

# Workflow

1. User enters a question in the Streamlit interface.
2. LangGraph classifies the intent.
3. Greeting and memory requests are handled directly.
4. University questions are routed to the RAG pipeline.
5. The Document Picker selects the relevant university documents.
6. Selected documents are chunked, embedded, and searched using FAISS.
7. Retrieved chunks are provided to the LLM.
8. The LLM generates an answer using only the retrieved context.
9. Responses requiring approval are presented through the Streamlit review interface.
10. The final answer is displayed together with its source documents.

---

# Knowledge Base

The assistant searches the following university documents:

- Academic Calendar
- Attendance Policy
- Grading Policy
- Hostel Rules
- Laboratory Guidelines
- Contact Directory

---

# Memory System

The assistant stores user memories inside:

```
code_pipeline/memory.json
```

Examples:

```
Remember my favourite subject is AI.
```

Later:

```
What do you remember about me?
```

---

# Human Review

Responses that involve:

- personal academic decisions
- permission requests
- missing information
- low-confidence retrieval

can be reviewed before being presented to the user.

---

# Running the Project

## Clone the repository

```bash
git clone <repository-url>
cd UNI-ASSISTANT
```

---

## Install dependencies

Windows

```bash
py -m pip install -r requirements.txt
```

Linux/macOS

```bash
python3 -m pip install -r requirements.txt
```

---

## Create a `.env` file

```
GROQ_API_KEY=your_groq_api_key
```

---

## Run the application

Windows

```bash
py -m streamlit run streamlit_app.py
```

Linux/macOS

```bash
python3 -m streamlit run streamlit_app.py
```

---

# Example Questions

Greeting

```
Hello
```

Attendance

```
What is the attendance policy?
```

Calendar

```
When are the final exams?
```

Laboratory

```
What happens if I break lab equipment?
```

Memory

```
Remember I am a Computer Science student.
```

Recall Memory

```
What do you remember about me?
```

Unknown

```
asdfghjkl
```

---

# Future Improvements

- Persistent FAISS index
- Conversation memory
- User authentication
- Multi-user support
- Hybrid retrieval
- Confidence scoring
- PDF knowledge base
- Database-backed memory
- Administrative dashboard

---

# Author

**Muhammad Ahmed Imran**

Built using Python, Streamlit, LangGraph, LangChain, Groq, and Retrieval-Augmented Generation (RAG).
