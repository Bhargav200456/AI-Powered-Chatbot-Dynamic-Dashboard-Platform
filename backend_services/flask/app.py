
import os
from flask import Flask, jsonify
from flask_cors import CORS
from dotenv import load_dotenv
import psycopg
from pathlib import Path

load_dotenv("../../.env")

app = Flask(__name__)
CORS(app)


def get_db_connection():
    return psycopg.connect(
        host=os.getenv("DB_HOST"),
        port=os.getenv("DB_PORT"),
        user=os.getenv("DB_USER"),
        password=os.getenv("DB_PASSWORD"),
        dbname=os.getenv("CHATBOT_DB")
    )


@app.route("/")
def home():
    return jsonify({
        "message": "Flask Backend is running!"
    })


@app.route("/health")
def health():
    return jsonify({
        "status": "healthy",
        "backend": "Flask"
    })


@app.route("/database")
def database():
    try:
        conn = get_db_connection()
        conn.close()

        return jsonify({
            "message": "Connected to chatbot_db"
        })

    except Exception as e:
        return jsonify({"error": str(e)}), 500


if __name__ == "__main__":
    app.run(host="127.0.0.1", port=5001, debug=True)
