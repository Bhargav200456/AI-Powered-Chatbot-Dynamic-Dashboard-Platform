
from fastapi import FastAPI
from pydantic import BaseModel

from chatbot.backend.agents.graph import chat

app = FastAPI(
    title="AI Chatbot API",
    version="1.0.0"
)


class ChatRequest(BaseModel):
    message: str


@app.get("/")
def home():
    return {"message": "AI Chatbot API is running!"}


@app.post("/chat")
async def chatbot_response(request: ChatRequest):
    response = await chat(request.message)

    return {
        "user_message": request.message,
        "ai_response": response
    }
