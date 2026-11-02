
const { Pool } = require("pg");
const dotenv = require("dotenv");
const path = require("path");

dotenv.config({
    path: path.resolve(__dirname, "../../../.env")
});

const pool = new Pool({
    host: process.env.DB_HOST,
    port: process.env.DB_PORT,
    user: process.env.DB_USER,
    password: process.env.DB_PASSWORD,
    database: process.env.NODEJS_DB
});

module.exports = pool;
