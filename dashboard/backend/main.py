
from fastapi import FastAPI
from pydantic import BaseModel
from dashboard.backend.agents.graph import generate_dashboard
app = FastAPI(
    title="Dynamic Dashboard API",
    version="1.0.0"
)


class DashboardRequest(BaseModel):
    request: str


@app.get("/")
def home():
    return {"message": "Dynamic Dashboard API is running!"}


@app.post("/generate")
async def create_dashboard(request: DashboardRequest):
    result = await generate_dashboard(request.request)

    return {
        "user_request": request.request,
        "dashboard_specification": result
    }
