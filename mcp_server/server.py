
import httpx
from mcp.server.fastmcp import FastMCP

mcp = FastMCP("Independent AI Applications MCP Server")

BACKENDS = {
    "nodejs": "http://localhost:5000",
    "flask": "http://localhost:5001",
    "fastapi": "http://localhost:5002"
}


@mcp.tool()
async def get_backend_status(backend: str) -> dict:
    """Get the health status of Node.js, Flask or FastAPI."""

    if backend not in BACKENDS:
        return {"error": "Invalid backend name"}

    async with httpx.AsyncClient() as client:
        try:
            response = await client.get(
                f"{BACKENDS[backend]}/health",
                timeout=10
            )
            response.raise_for_status()
            return response.json()

        except httpx.HTTPError as e:
            return {"error": str(e)}


@mcp.tool()
async def get_backend_data(backend: str) -> dict:
    """Retrieve information from a selected backend."""

    if backend not in BACKENDS:
        return {"error": "Invalid backend name"}

    async with httpx.AsyncClient() as client:
        try:
            response = await client.get(
                f"{BACKENDS[backend]}/",
                timeout=10
            )
            response.raise_for_status()
            return response.json()

        except httpx.HTTPError as e:
            return {"error": str(e)}


@mcp.tool()
def get_available_backends() -> list:
    """List all available backend services."""

    return [
        {
            "name": "Node.js",
            "database": "nodejs_db",
            "url": BACKENDS["nodejs"]
        },
        {
            "name": "Flask",
            "database": "chatbot_db",
            "url": BACKENDS["flask"]
        },
        {
            "name": "FastAPI",
            "database": "dashboard_db",
            "url": BACKENDS["fastapi"]
        }
    ]


if __name__ == "__main__":
    mcp.run()
