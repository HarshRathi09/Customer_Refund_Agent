from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from api.routes import router


app = FastAPI(
    title="AI Customer Support Agent",
    description="AI-powered customer support and refund processing agent using LangGraph, Groq, RAG, and tool calling.",
    version="1.0.0"
)


app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"]
)


@app.get("/")
def root():
    return {
        "message": "AI Customer Support Agent API is running"
    }


app.include_router(router)