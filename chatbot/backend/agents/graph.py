
from langgraph.prebuilt import create_react_agent

from shared.llm import get_llm
from shared.mcp_client import get_mcp_tools


async def create_chatbot():
    llm = get_llm()

    tools = await get_mcp_tools()

    agent = create_react_agent(
        model=llm,
        tools=tools,
        prompt=(
            "You are an intelligent AI assistant. "
            "Help users with their questions. "
            "Use the available MCP tools whenever "
            "backend information is required. "
            "Explain results clearly."
        )
    )

    return agent


async def chat(message: str):
    agent = await create_chatbot()

    response = await agent.ainvoke({
        "messages": [
            {"role": "user", "content": message}
        ]
    })

    return response["messages"][-1].content
