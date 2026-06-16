# app/routes/chat.py

from fastapi import APIRouter
from app.services.rag_service import answer_question
from app.models.chat_models import ChatRequest
from app.services.gemini_service import ask_gemini

router = APIRouter()


@router.post("/chat")
def chat(request: ChatRequest):

    answer = answer_question(request.question)

    return {
        "answer": answer
    }