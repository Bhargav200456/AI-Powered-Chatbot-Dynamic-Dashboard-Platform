
import os
from fastapi import FastAPI
from dotenv import load_dotenv
import psycopg

load_dotenv("../../.env")

app = FastAPI(
    title="AI Applications FastAPI Backend",
    version="1.0.0"
)


def get_db_connection():
    return psycopg.connect(
        host=os.getenv("DB_HOST"),
        port=os.getenv("DB_PORT"),
        user=os.getenv("DB_USER"),
        password=os.getenv("DB_PASSWORD"),
        dbname=os.getenv("DASHBOARD_DB")
    )


@app.get("/")
def home():
    return {
        "message": "FastAPI Backend is running!"
    }


@app.get("/health")
def health():
    return {
        "status": "healthy",
        "backend": "FastAPI"
    }


@app.get("/database")
def database():
    try:
        conn = get_db_connection()
        conn.close()

        return {
            "message": "Connected to dashboard_db"
        }

    except Exception as e:
        return {"error": str(e)}
