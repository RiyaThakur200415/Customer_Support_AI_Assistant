# AI-Powered Customer Support Automation System

## Project Description

The **AI-Powered Customer Support Automation System** is a multi-agent application developed using **LangGraph** to automate customer support operations for **ABC Technologies**, a SaaS company.

The system accepts customer queries, classifies the intent, routes requests to specialized support agents, retrieves relevant information using a Retrieval-Augmented Generation (RAG) pipeline, maintains customer conversation history using SQLite, and handles high-risk requests through a Human-in-the-Loop approval process.

This project demonstrates how Large Language Models (LLMs), LangGraph, FAISS, SQLite, and Ollama can be combined to build an intelligent customer support assistant.

---

# Features

* Intent Classification
* Multi-Agent Workflow using LangGraph
* Sales Support Agent
* Technical Support Agent
* Billing Support Agent
* Account Support Agent
* Memory Agent
* Supervisor Agent
* FAISS-based RAG
* SQLite Conversation Memory
* Human-in-the-Loop Approval
* Streamlit User Interface
* Local LLM using Ollama (Qwen2.5:3B)

---

# Technologies Used

* Python 3.x
* LangGraph
* LangChain
* LangChain-Ollama
* FAISS
* SQLite
* Streamlit
* Ollama
* Qwen2.5:3B
* Nomic Embed Text Embeddings

---

# Project Structure

```text
AI Powered Support System/
│
├── app.py
├── frontend.py
├── requirements.txt
├── README.md
│
├── agents/
├── graph/
├── memory/
├── nodes/
├── rag/
└── utils/
```

---

# Setup Instructions

## Step 1: Clone or Download the Project

Download the project or clone it using Git.

---

## Step 2: Install Python Packages

```bash
pip install -r requirements.txt
```

Or install manually:

```bash
pip install streamlit
pip install langgraph
pip install langchain
pip install langchain-community
pip install langchain-ollama
pip install langchain-text-splitters
pip install faiss-cpu
pip install pypdf
```

---

## Step 3: Install Ollama

Download and install Ollama.

Pull the required models:

```bash
ollama pull qwen2.5:3b

ollama pull nomic-embed-text
```

---

## Step 4: Create the FAISS Vector Database

Run the following command once:

```bash
python rag/vector_store.py
```

This creates:

```
rag/faiss_index/
    index.faiss
    index.pkl
```

---

## Step 5: Run the Application

### Console Version

```bash
python app.py
```

### Streamlit Version

```bash
streamlit run app.py
```

---

# Sample Queries

### Sales

```
What are the pricing plans available?
```

---

### Account

```
I forgot my account password.
```

---

### Technical

```
My application crashes whenever I upload a file.
```

---

### Billing

```
I need a refund for my annual subscription.
```

---

### Memory

```
What was my previous support issue?
```

---

# Workflow

1. Customer submits a query.
2. Intent Classifier identifies the department.
3. Query is routed to the appropriate support agent.
4. The agent retrieves relevant information using FAISS-based RAG.
5. High-risk requests are sent for Human Approval.
6. Supervisor Agent validates the response.
7. Conversation is stored in SQLite.
8. Final response is returned to the customer.

---

# Human-in-the-Loop Requests

The following requests require manual approval:

* Refund Requests
* Subscription Cancellation
* Account Closure
* Compensation Requests
* Escalation to Management

---

# RAG Documents

The system retrieves information from:

* Company Policy
* Pricing Guide
* Technical Manual
* FAQ Document

---

# Memory

Customer conversations are stored in SQLite with:

* Customer Name
* Query
* Department
* Response
* Timestamp

The chatbot can recall previous customer interactions when requested.

---

# Expected Output

The application displays:

* Customer Query
* Detected Department
* Retrieved RAG Context
* Human Approval Status
* Conversation History
* Final Customer Response

---

# Author

**Riya Kumari**

B.Tech – Computer Science and Engineering

AI-Powered Customer Support Automation System using LangGraph
