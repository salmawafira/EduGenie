from fastapi import FastAPI
from fastapi.responses import FileResponse
from pydantic import BaseModel

app = FastAPI(title="EduGenie")


class Question(BaseModel):
    task: str
    question: str


@app.get("/")
def home():
    return FileResponse("index.html")


@app.post("/ask")
def ask_question(data: Question):
    answers = {
        "Explain": f"Explanation: {data.question} is an important topic. EduGenie explains it in simple terms.",
        "Q&A": f"Answer: EduGenie received your question about {data.question}.",
        "Quiz": f"Quiz: Here is a quiz topic based on {data.question}.",
        "Summary": f"Summary: This is a simple summary of {data.question}.",
        "Recommend Path": f"Learning Path: Start with the basics of {data.question}, then practice with examples."
    }

    return {
        "question": data.question,
        "answer": answers.get(data.task, "Please select a task.")
    }