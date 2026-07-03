# 🤖 AI-Powered Customer Support Automation System

An intelligent customer support assistant that automates customer query handling using a multi-agent workflow. The application classifies customer queries, retrieves relevant information from a knowledge base using Retrieval-Augmented Generation (RAG), maintains conversation history, and generates context-aware responses through an interactive Streamlit interface.

---

## 📌 Features

- 🤖 AI-powered customer support assistant
- 🧠 Multi-agent workflow orchestration using LangGraph
- 📚 Retrieval-Augmented Generation (RAG) with FAISS
- 💬 Context-aware response generation
- 📝 Conversation history using SQLite
- 🎯 Automatic intent classification
- 🔄 Approval workflow for sensitive customer requests
- 🌐 Interactive Streamlit web interface
- ⚡ Semantic search over knowledge base

---

# 🏗️ System Architecture

```text
                              ┌──────────────────────────┐
                              │        Customer          │
                              │      Streamlit UI        │
                              └────────────┬─────────────┘
                                           │
                                           ▼
                          ┌────────────────────────────────┐
                          │      Customer Query Input      │
                          │   Name + Support Request       │
                          └────────────┬───────────────────┘
                                       │
                                       ▼
                          ┌────────────────────────────────┐
                          │      LangGraph Workflow        │
                          └────────────┬───────────────────┘
                                       │
          ┌────────────────────────────┼────────────────────────────┐
          │                            │                            │
          ▼                            ▼                            ▼
 ┌──────────────────┐        ┌────────────────────┐      ┌───────────────────┐
 │ Intent Detection │        │ RAG Retrieval      │      │ Conversation Memory│
 │                  │        │                    │      │                   │
 │ • Sales          │        │ • FAISS Index      │      │ • SQLite Database │
 │ • Billing        │        │ • Knowledge Base   │      │ • Previous Chats  │
 │ • Tech Support   │        │                    │      │                   │
 │ • Account        │        └─────────┬──────────┘      └─────────┬─────────┘
 └─────────┬────────┘                  │                           │
           └───────────────┬───────────┴───────────────┬───────────┘
                           │                           │
                           ▼
                ┌─────────────────────────────┐
                │ Response Generation Engine  │
                │ Intent + Context + Memory   │
                └──────────────┬──────────────┘
                               │
                               ▼
                ┌─────────────────────────────┐
                │  Customer Support Response  │
                │ Department │ Approval │ Reply│
                └──────────────┬──────────────┘
                               │
                               ▼
                     ┌──────────────────────┐
                     │ Display in Streamlit │
                     └──────────────────────┘
```

---

# 🔄 Workflow

```text
Customer
    │
    ▼
Enter Name & Query
    │
    ▼
LangGraph Workflow
    │
    ├────────► Detect Intent
    │
    ├────────► Retrieve Relevant Documents
    │            (FAISS Vector Store)
    │
    ├────────► Load Previous Conversation
    │            (SQLite)
    │
    ├────────► Generate Context-Aware Response
    │
    ▼
Display Response
```

---

# 📂 Project Structure

```text
Customer_Support_AI_Assistant/
│
├── frontend.py                # Streamlit UI
├── app.py                     # Application entry point
├── requirements.txt
│
├── graph/
│   └── workflow.py
│
├── nodes/
│   ├── classify_intent.py
│   ├── retrieve_context.py
│   ├── generate_response.py
│   ├── approval.py
│   └── memory.py
│
├── rag/
│   ├── vector_store.py
│   └── retriever.py
│
├── memory/
│   └── database.py
│
├── knowledge_base/
│   ├── sales.txt
│   ├── billing.txt
│   ├── technical_support.txt
│   └── account.txt
│
└── README.md
```

---

# 🛠️ Tech Stack

| Category | Technologies |
|----------|--------------|
| Programming Language | Python |
| User Interface | Streamlit |
| Workflow Orchestration | LangGraph |
| AI Framework | LangChain |
| Vector Database | FAISS |
| Memory | SQLite |
| Knowledge Retrieval | Retrieval-Augmented Generation (RAG) |

---

# 🚀 Installation

## Clone the Repository

```bash
git clone https://github.com/RiyaThakur200415/Customer_Support_AI_Assistant.git
```

Move into the project directory

```bash
cd Customer_Support_AI_Assistant
```

---

## Create Virtual Environment

Windows

```bash
python -m venv venv
venv\Scripts\activate
```

Linux / macOS

```bash
python3 -m venv venv
source venv/bin/activate
```

---

## Install Dependencies

```bash
pip install -r requirements.txt
```

---

# ▶️ Run the Application

```bash
streamlit run frontend.py
```

The application will start on

```
http://localhost:8501
```

---

# 💼 Supported Departments

- 💰 Sales
- 💳 Billing
- 💻 Technical Support
- 👤 Account Management

---

# 📸 Screenshots

Create an **assets** folder and add screenshots.

```text
assets/
│
├── homepage.png
├── response.png
└── architecture.png
```

Display them in README.

```markdown
## Home Page

![Homepage](assets/homepage.png)

## Generated Response

![Response](assets/response.png)

## Architecture

![Architecture](assets/architecture.png)
```

---

# 🎯 Future Improvements

- User Authentication
- Ticket Generation
- Admin Dashboard
- Email Notifications
- Analytics Dashboard
- Cloud Deployment
- Multi-language Support

---

# 👩‍💻 Author

**Riya Kumari**

GitHub: https://github.com/RiyaThakur200415

---

# ⭐ Support

If you found this project helpful, consider giving it a ⭐ on GitHub.
