
import sys
from pathlib import Path
from langchain_mcp_adapters.client import MultiServerMCPClient

ROOT_DIR = Path(__file__).resolve().parent.parent
MCP_SERVER_PATH = ROOT_DIR / "mcp_server" / "server.py"


async def get_mcp_tools():
    client = MultiServerMCPClient(
        {
            "backend_services": {
                "command": sys.executable,
                "args": [str(MCP_SERVER_PATH)],
                "transport": "stdio"
            }
        }
    )

    tools = await client.get_tools()
    return tools
