import os
from dotenv import load_dotenv
# from openai import OpenAI
from groq import Groq

load_dotenv()

client = Groq(
    api_key=os.getenv("GROQ_API_KEY"),
    # base_url="https://generativelanguage.googleapis.com/v1beta/"
)

def ask(prompt):
    response = client.chat.completions.create(
        model="llama-3.1-8b-instant",
        messages=[{"role": "user", "content": prompt}]
    )
    return response.choices[0].message.content