from pydantic import BaseModel


class ChatRequest(BaseModel):
    message: str


class ChatResponse(BaseModel):
    decision: str
    category: str
    reason: str
    explanation: str
    logs: list[str]
    