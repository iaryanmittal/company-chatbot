# app/core/config.py

import os
from dotenv import load_dotenv

load_dotenv()

GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")

MODEL_NAME = "gemini-2.5-flash"

CHROMA_PATH = "./chroma_db"

DISTANCE_THRESHOLD = 1.5