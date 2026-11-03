# AI-Powered Chatbot & Dynamic Dashboard Platform

An AI application platform that combines a conversational chatbot and a
dynamic dashboard. The project uses LangGraph to orchestrate AI
workflows, an independent MCP server to expose backend tools, and three
backend services built with Node.js, Flask, and FastAPI. Each backend
service is connected to its own PostgreSQL database.

> **Project status:** In development. Some integrations and frontend
> features are still being built.

## Key Features

-   **AI Chatbot:** Conversational interface powered by Llama 3.1
    through Ollama.
-   **Dynamic Dashboard:** Designed to generate relevant KPIs, charts,
    and tables from natural-language requests.
-   **LangGraph workflows:** Used to coordinate the chatbot and
    dashboard agent workflows.
-   **MCP integration:** A separate MCP server exposes reusable tools
    for communication with backend services.
-   **Multiple backend services:** Node.js, Flask, and FastAPI run as
    independent services.
-   **Separate databases:** Each backend service has its own PostgreSQL
    database.
-   **Configurable LLM provider:** A shared LLM configuration layer is
    designed to support switching from Ollama to OpenAI through
    environment settings.

## Technology Stack

  Area                 Technologies
  -------------------- -----------------------------------
  AI orchestration     LangGraph, LangChain
  LLM                  Llama 3.1, Ollama; OpenAI planned
  Tool integration     Model Context Protocol (MCP)
  Backend services     Node.js, Flask, FastAPI
  Databases            PostgreSQL
  Python environment   Python virtual environment
  Node environment     Node.js, npm

## Architecture Overview

``` text
                       +----------------------+
                       |   AI Applications    |
                       |                      |
                       |  Chatbot  Dashboard  |
                       |  LangGraph workflows |
                       +----------+-----------+
                                  |
                         Shared MCP Client
                                  |
                       +----------v-----------+
                       |    Independent MCP   |
                       |        Server        |
                       +---+--------+-----+---+
                           |        |     |
                    +------v+  +----v--+  +v---------+
                    |Node.js|  | Flask |  | FastAPI  |
                    | :5000 |  | :5001 |  | :5002    |
                    +---+---+  +---+---+  +----+-----+
                        |          |          |
                    nodejs_db  chatbot_db  dashboard_db
```

The MCP server communicates with backend services through their HTTP
APIs. Each backend service owns its own database connection.

## Project Structure

``` text
AI_Applications/
├── backend_services/
│   ├── nodejs/
│   │   └── src/
│   │       ├── server.js
│   │       ├── db.js
│   │       └── test-db.js
│   ├── flask/
│   │   └── app.py
│   └── fastapi/
│       └── main.py
├── chatbot/
│   └── backend/
│       ├── agents/
│       │   └── graph.py
│       ├── api/
│       ├── database/
│       └── main.py
├── dashboard/
│   └── backend/
│       ├── agents/
│       │   └── graph.py
│       ├── api/
│       ├── database/
│       └── main.py
├── mcp_server/
│   ├── tools/
│   ├── database/
│   └── server.py
├── shared/
│   ├── llm.py
│   ├── mcp_client.py
│   └── config.py
├── .env.example
├── requirements.txt
└── test_mcp.py
```

## Prerequisites

Install the following before running the project:

-   Python 3.10 or later
-   Node.js and npm
-   PostgreSQL
-   Ollama
-   Git

Make sure PostgreSQL and Ollama are running before starting the
application.

## 1. Clone the Repository

``` powershell
git clone https://github.com/Bhargav200456/AI-Powered-Chatbot-Dynamic-Dashboard-Platform.git
cd AI-Powered-Chatbot-Dynamic-Dashboard-Platform
```

## 2. Create and Activate the Python Virtual Environment

Run these commands from the project root:

``` powershell
python -m venv .venv
.venv\Scripts\Activate.ps1
```

If PowerShell blocks activation, use this for the current terminal
session:

``` powershell
Set-ExecutionPolicy -Scope Process -ExecutionPolicy Bypass
.venv\Scripts\Activate.ps1
```

## 3. Install Python Dependencies

``` powershell
python -m pip install --upgrade pip
pip install -r requirements.txt
```

## 4. Install Node.js Dependencies

``` powershell
cd backend_services\nodejs
npm install
cd ..\..
```

## 5. Configure Environment Variables

Create a `.env` file in the project root using `.env.example` as the
reference.

Example configuration:

``` env
# LLM Configuration
LLM_PROVIDER=ollama
LLM_MODEL=llama3.1:8b

# Ollama
OLLAMA_BASE_URL=http://localhost:11434

# OpenAI (for a future provider switch)
OPENAI_API_KEY=
OPENAI_MODEL=gpt-4.1-mini

# PostgreSQL
DB_HOST=localhost
DB_PORT=5432
DB_USER=postgres
DB_PASSWORD=YOUR_POSTGRES_PASSWORD

# Database names
NODEJS_DB=nodejs_db
CHATBOT_DB=chatbot_db
DASHBOARD_DB=dashboard_db

# Backend service ports
NODE_PORT=5000
FLASK_PORT=5001
FASTAPI_PORT=5002
```

Replace `YOUR_POSTGRES_PASSWORD` with your local PostgreSQL password. Do
not commit `.env` or expose database credentials or API keys. Only
commit `.env.example` with placeholder values.

Create these three databases in PostgreSQL if they do not already exist:

-   `nodejs_db`
-   `chatbot_db`
-   `dashboard_db`

## 6. Set Up the Local LLM

Download the model once:

``` powershell
ollama pull llama3.1:8b
```

Start Ollama if it is not already running. You can verify the model
with:

``` powershell
ollama run llama3.1:8b
```

Exit the interactive model prompt when finished. Keep the Ollama service
running while using the AI applications.

## Running the Project

Start each service in a **separate PowerShell terminal**. Keep the
terminals open while using the applications. Activate the root `.venv`
in each terminal that runs Python.

### Terminal 1 --- Node.js Backend (port 5000)

``` powershell
cd C:\Users\<YOUR_USER>\Documents\AI_Applications\backend_services\nodejs
node src/server.js
```

### Terminal 2 --- Flask Backend (port 5001)

``` powershell
cd C:\Users\<YOUR_USER>\Documents\AI_Applications
.venv\Scripts\Activate.ps1
cd backend_services\flask
python app.py
```

### Terminal 3 --- FastAPI Backend Service (port 5002)

``` powershell
cd C:\Users\<YOUR_USER>\Documents\AI_Applications
.venv\Scripts\Activate.ps1
cd backend_services\fastapi
python -m uvicorn main:app --reload --port 5002
```

### Terminal 4 --- AI Chatbot API (port 8000)

Run from the project root so Python can resolve the project packages:

``` powershell
cd C:\Users\<YOUR_USER>\Documents\AI_Applications
.venv\Scripts\Activate.ps1
python -m uvicorn chatbot.backend.main:app --reload --port 8000
```

### Terminal 5 --- Dynamic Dashboard API (port 8001)

Run from the project root:

``` powershell
cd C:\Users\<YOUR_USER>\Documents\AI_Applications
.venv\Scripts\Activate.ps1
python -m uvicorn dashboard.backend.main:app --reload --port 8001
```

The shared MCP client starts the MCP server as a subprocess over
standard input/output when an AI agent requests its tools. You do not
normally need to start a separate MCP terminal for the chatbot or
dashboard.

### Optional --- Run the MCP Server Directly

For standalone inspection or development:

``` powershell
cd C:\Users\<YOUR_USER>\Documents\AI_Applications
.venv\Scripts\Activate.ps1
python mcp_server\server.py
```

When run directly, the MCP server uses standard input/output transport
and may appear to wait for MCP client input. This is expected.

## Service URLs

  Service                URL
  ---------------------- ----------------------------
  Node.js backend        http://localhost:5000
  Flask backend          http://localhost:5001
  FastAPI backend        http://localhost:5002
  Chatbot API            http://localhost:8000
  Dashboard API          http://localhost:8001
  FastAPI backend docs   http://localhost:5002/docs
  Chatbot API docs       http://localhost:8000/docs
  Dashboard API docs     http://localhost:8001/docs

## Health Checks

Run these from another PowerShell terminal:

``` powershell
Invoke-RestMethod http://localhost:5000/health
Invoke-RestMethod http://localhost:5001/health
Invoke-RestMethod http://localhost:5002/health
```

Expected result: each backend returns a healthy status.

## Test MCP Tool Discovery and Backend Communication

With the three backend services running, open a new terminal at the
project root:

``` powershell
cd C:\Users\<YOUR_USER>\Documents\AI_Applications
.venv\Scripts\Activate.ps1
python test_mcp.py
```

The test should discover the MCP tools and retrieve the health status of
Node.js, Flask, and FastAPI.

## API Usage

### Chatbot

Endpoint:

``` text
POST http://localhost:8000/chat
```

Example PowerShell request:

``` powershell
$body = @{
    message = "Explain artificial intelligence in two sentences."
} | ConvertTo-Json

Invoke-RestMethod `
    -Uri "http://localhost:8000/chat" `
    -Method Post `
    -ContentType "application/json" `
    -Body $body
```

### Dynamic Dashboard

Endpoint:

``` text
POST http://localhost:8001/generate
```

Example PowerShell request:

``` powershell
$body = @{
    request = "Create a dashboard showing monthly sales KPIs and a sales trend chart."
} | ConvertTo-Json

Invoke-RestMethod `
    -Uri "http://localhost:8001/generate" `
    -Method Post `
    -ContentType "application/json" `
    -Body $body
```

## Switching the LLM Provider

The shared LLM provider is configured through the root `.env` file.

For local Ollama:

``` env
LLM_PROVIDER=ollama
LLM_MODEL=llama3.1:8b
OLLAMA_BASE_URL=http://localhost:11434
```

For OpenAI, when API access is configured:

``` env
LLM_PROVIDER=openai
OPENAI_API_KEY=YOUR_OPENAI_API_KEY
OPENAI_MODEL=gpt-4.1-mini
```

Restart the relevant AI application after changing provider settings.
Never commit real API keys.

## Troubleshooting

-   **Python module not found:** Confirm that `.venv` is activated and
    run commands from the specified working directory.
-   **Connection refused:** Confirm that the relevant backend service,
    PostgreSQL, or Ollama is running and that the configured port is
    correct.
-   **Database connection error:** Verify the database names, PostgreSQL
    username, password, host, and port in `.env`.
-   **MCP tools cannot reach a backend:** Start the three backend
    services before testing MCP communication.
-   **Ollama model not found:** Run `ollama pull llama3.1:8b`.
-   **Port already in use:** Stop the other process using that port or
    configure a different port consistently.

## Development Notes

-   The three backend services are independent and each owns its
    PostgreSQL database.
-   MCP provides a common tool interface for AI applications to
    communicate with backend services.
-   LangGraph is used to orchestrate the chatbot and dashboard
    workflows.
-   The dashboard is intended to adapt its visualizations to the user's
    natural-language request.
-   Frontend setup commands are not included here because the frontend
    implementation and package scripts are not yet confirmed.

## Author

**Bhargav K.**

GitHub: [Bhargav200456](https://github.com/Bhargav200456)
