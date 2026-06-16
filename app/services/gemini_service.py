# app/services/gemini_service.py

from google import genai
from dotenv import load_dotenv
import os

load_dotenv()

client = genai.Client(
    api_key=os.getenv("GEMINI_API_KEY")
)


def ask_gemini(question: str):

    try:

        response = client.models.generate_content(
            model="gemini-2.5-flash",
            contents=question
        )

        return response.text

    except Exception as e:

        print("Gemini Error:", e)

        return "The AI service is temporarily unavailable. Please try again later."

    return response.text