from dotenv import load_dotenv

from langchain_core.messages import (
    SystemMessage
)

from langchain_groq import ChatGroq

from langgraph.prebuilt import ToolNode

from agent.prompts import SYSTEM_PROMPT

from agent.tools import (
    get_customer,
    get_order,
    retrieve_policy
)

load_dotenv()

TOOLS = [
    get_customer,
    get_order,
    retrieve_policy
]

llm = ChatGroq(
    model="llama-3.3-70b-versatile",
    temperature=0
)

llm_with_tools = llm.bind_tools(
    TOOLS
)

tool_node = ToolNode(
    TOOLS
)

def agent_node(state):

    messages = state["messages"]

    response = llm_with_tools.invoke(
        [
            SystemMessage(
                content=SYSTEM_PROMPT
            )
        ]
        + messages
    )

    return {
        "messages": [response]
    }

def should_continue(state):

    last_message = state["messages"][-1]

    if hasattr(last_message, "tool_calls"):

        if len(last_message.tool_calls) > 0:

            return "tools"

    return "end"