# app/models/chat_models.py

from pydantic import BaseModel

class ChatRequest(BaseModel):
    question: str