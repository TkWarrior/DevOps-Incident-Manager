from fastapi import FastAPI
from main import run_agent
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()
history = []

@app.post("/run")
def run():
    result = run_agent()
    history.append(result)
    return result

@app.get("/incidents")
def incidents():
    return history

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173"],
    allow_methods=["*"],
    allow_headers=["*"],
)