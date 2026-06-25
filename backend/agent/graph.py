from langgraph.graph import (
    StateGraph,
    END
)

from agent.state import AgentState

from agent.nodes import (
    agent_node,
    tool_node,
    should_continue
)

builder = StateGraph(
    AgentState
)

builder.add_node(
    "agent",
    agent_node
)

builder.add_node(
    "tools",
    tool_node
)

builder.set_entry_point(
    "agent"
)

builder.add_conditional_edges(
    "agent",
    should_continue,
    {
        "tools": "tools",
        "end": END
    }
)

builder.add_edge(
    "tools",
    "agent"
)

# Compile graph
refund_graph = builder.compile()