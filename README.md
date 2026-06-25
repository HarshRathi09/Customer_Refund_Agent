 Customer AI Refund Agent

An AI-powered customer support agent that automates refund decision-making using LangGraph, Retrieval-Augmented Generation (RAG), FAISS Vector Database, FastAPI, SQLite, and React.

The agent retrieves customer information, order details, and company refund policies before making a decision, ensuring responses are grounded in real data rather than assumptions.

---

## Features

- AI Agent powered by LangGraph
- Retrieval-Augmented Generation (RAG)
- FAISS Vector Database for policy retrieval
- SQLite Database for customer and order management
- FastAPI Backend
- React + Vite Frontend
- Structured JSON Responses
- Business-rule-based refund decisions
- Tool-calling architecture

---

## Project Architecture

```text
User
  │
  ▼
React Frontend
  │
  ▼
FastAPI Backend
  │
  ▼
LangGraph Agent
  │
  ├── Get Order Details
  ├── Get Customer Details
  └── Retrieve Refund Policy (RAG)
  │
  ▼
Decision Engine
  │
  ▼
Structured JSON Response
```

---

Tech Stack

--> BACKEND

- Python
- FastAPI
- LangGraph
- LangChain
- SQLAlchemy
- SQLite

-> AI & RAG

- HuggingFace Embeddings
- sentence-transformers/all-MiniLM-L6-v2
- FAISS
- Retrieval-Augmented Generation (RAG)

-> FRONTEND

- React
- Vite
- JavaScript
- CSS

---

-> REFUND WORKFLOW

The agent follows the workflow below:

1. User submits a refund request.
2. Agent retrieves order information.
3. Agent extracts the customer ID.
4. Agent retrieves customer information.
5. Agent retrieves relevant refund policies using RAG.
6. Agent evaluates eligibility.
7. Agent returns a structured decision.

---

## Example Policies

```text
Refunds allowed within 30 days.

Electronics:
Refund only within 15 days.

Opened electronics:
No refund.

More than 3 refunds:
Denied.

Damaged products:
Always approved.
```

---

## Example Request

```json
{
  "message": "I want a refund for ORD1003"
}
```

---

Example Response

json
{
  "decision": "APPROVED",
  "policy_rule": "Damaged products are always approved.",
  "reason": "The product is damaged.",
  "explanation": "According to company policy, damaged products qualify for an automatic refund. Therefore the refund request has been approved.",
  "logs": []
}



Setup Instructions

->BACKEND

Create virtual environment

```bash
python -m venv venv
```

ACTIVATE ENVIRONMENT

```bash
venv\Scripts\activate
```

INSTALL DEPENDENCIES

```bash
pip install -r requirements.txt
```

SEED DATABASE

```bash
python -m data.seed
```

Create FAISS index

```bash
python create_index.py
```

RUN BACKEND

```bash
uvicorn main:app --reload
```

Backend available at:

```text
http://localhost:8000
```

Swagger Docs:

```text
http://localhost:8000/docs
```

---

FRONTEND

Install dependencies

```bash
npm install
```

Run application

```bash
npm run dev
```

Frontend available at:

```text
http://localhost:5173
```

---

## Sample Test Cases

### ORD1001

Opened Electronics

Result:

```json
{
  "decision": "DENIED"
}
```

---

### ORD1002

More than 3 Refunds

Result:

```json
{
  "decision": "DENIED"
}
```

---

 ORD1003

Damaged Product

Result:

```json
{
  "decision": "APPROVED"
}
```


AI/ML Developer | Generative AI | LLM Applications | RAG Systems | AI Agents
