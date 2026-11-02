import asyncio
from shared.mcp_client import get_mcp_tools


async def main():
    tools = await get_mcp_tools()

    for tool in tools:
        if tool.name == "get_backend_status":
            for backend in ["nodejs", "flask", "fastapi"]:
                result = await tool.ainvoke({
                    "backend": backend
                })

                print(f"{backend}: {result}")


if __name__ == "__main__":
    asyncio.run(main())