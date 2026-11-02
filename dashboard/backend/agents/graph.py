
from langgraph.prebuilt import create_react_agent

from shared.llm import get_llm
from shared.mcp_client import get_mcp_tools


async def create_dashboard_agent():
    llm = get_llm()

    tools = await get_mcp_tools()

    agent = create_react_agent(
        model=llm,
        tools=tools,
        prompt=(
            "You are an intelligent dynamic dashboard agent. "
            "Understand the user's dashboard requirements. "
            "Identify the relevant KPIs, charts, tables, "
            "and other visualizations requested. "
            "Use available MCP tools when backend information "
            "is required. "
            "Do not suggest irrelevant visualizations. "
            "Return a clear, structured dashboard specification "
            "that the frontend can use to render the dashboard."
        )
    )

    return agent


async def generate_dashboard(request: str):
    agent = await create_dashboard_agent()

    response = await agent.ainvoke({
        "messages": [
            {"role": "user", "content": request}
        ]
    })

    return response["messages"][-1].content
