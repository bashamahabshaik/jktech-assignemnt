# Book Review App (Flask + Postgres + Ollama)
This project is a full-stack Python application using **Flask**, **PostgreSQL**, and **Ollama** for handling book reviews and AI-generated interactions.

---

## 🚀 Features

- Flask async backend
- PostgreSQL for persistent storage
- Automatically seeds 25 books and 100 reviews on startup
- Async communication with [Ollama](https://ollama.com/) (local AI model API)
- Dockerized environment

---

## 🧱 Requirements

- [Docker](https://www.docker.com/)
- [Ollama](https://ollama.com/) installed locally and running the `llama3:8b` model
- Python 3.12 (only if running outside Docker)

---

## 🛠️ Setup Instructions

### 1. 🧠 Start Ollama locally

Make sure Ollama is running and listening on port `11434` on your **host machine**.

```bash
ollama run llama3:8b
```
Ollama must be running before starting the Docker containers.

## Build and Run with Docker
```bash
docker-compose up --build
```
## Access the App
```bash
http://localhost:5000/
```
