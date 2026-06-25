from fastapi import APIRouter
from langchain_core.messages import HumanMessage

from agent.graph import refund_graph

from schemas.chat import (
    ChatRequest,
    ChatResponse
)

import json

router = APIRouter()


@router.post(
    "/chat",
    response_model=ChatResponse
)
def chat(request: ChatRequest):

    result = refund_graph.invoke(
        {
            "messages": [
                HumanMessage(
                    content=request.message
                )
            ]
        }
    )

    final_message = result["messages"][-1]

    response_data = json.loads(
        final_message.content
    )

    return ChatResponse(
        decision=response_data["decision"],
        category=response_data["category"],
        reason=response_data["reason"],
        explanation=response_data["explanation"],
        logs=[]
    )