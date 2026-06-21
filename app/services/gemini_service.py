# app/services/gemini_service.py

from google import genai
from dotenv import load_dotenv
import os

load_dotenv()

API_KEYS = [
    os.getenv("GEMINI_API_KEY_1"),
    os.getenv("GEMINI_API_KEY_2"),
    os.getenv("GEMINI_API_KEY_3"),
    os.getenv("GEMINI_API_KEY_4")
]

# Remove empty keys
API_KEYS = [key for key in API_KEYS if key]


def ask_gemini(question: str):

    last_error = None

    for i, api_key in enumerate(API_KEYS):

        try:

            print(f"Trying Gemini Key {i+1}")

            client = genai.Client(
                api_key=api_key
            )

            response = client.models.generate_content(
                model="gemini-2.5-flash",
                contents=question
            )

            print(f"Success with Key {i+1}")

            return response.text

        except Exception as e:

            print(f"Key {i+1} Failed:")
            print(e)

            last_error = e

            continue

    print("All Gemini Keys Failed")
    print(last_error)

    return (
        "The AI service is temporarily unavailable. "
        "Please try again in a few minutes."
    )