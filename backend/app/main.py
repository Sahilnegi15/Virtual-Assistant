from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from agents import handle_query
from multi_agents import multi_agent_pipeline

app = FastAPI(title="Smart Research Assistant")

# Allow React frontend to access FastAPI
origins = [
    "http://localhost:3000",  # React dev server
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class Query(BaseModel):
    question: str

@app.get("/")
def home():
    return {"message": "Smart Research Assistant API is running."}

@app.post("/ask")
def ask_question(query: Query):
    answer = handle_query(query.question)
    return {"answer": answer}

@app.get("/run-task")
def run_task():
    from automation import smart_research_task
    smart_research_task()
    return {"message": "Task executed"}


@app.post("/multi-agent")
def multi_agent(query: Query):
    answer = multi_agent_pipeline(query.question)
    return {"answer": answer}

@app.post("/login")
async def login(email: str = Form(...), password: str = Form(...)):
    # Replace with real authentication logic
    if email == "test@example.com" and password == "password123":
        return {"success": True, "message": "Login successful!"}
    return {"success": False, "message": "Invalid credentials"}