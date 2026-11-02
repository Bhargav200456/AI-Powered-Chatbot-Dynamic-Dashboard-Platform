
const express = require("express");
const cors = require("cors");
require("dotenv").config();

const app = express();

app.use(cors());
app.use(express.json());

app.get("/", (req, res) => {
    res.json({
        message: "Node.js Backend is running successfully!"
    });
});

app.get("/health", (req, res) => {
    res.json({
        status: "healthy",
        backend: "Node.js",
        database: "PostgreSQL"
    });
});

const PORT = process.env.NODE_PORT || 5000;

app.listen(PORT, () => {
    console.log(`Node.js server running on http://localhost:${PORT}`);
});
