import os
from openai import OpenAI, DefaultHttpxClient
import httpx

client = OpenAI(
    # Or use the `OPENAI_BASE_URL` env var
    base_url="http://localhost:8000",
    api_key="llama.cpp"
)

chat_completion = client.chat.completions.create(
    messages=[
        {
            "role": "user",
            "content": "Say this is a test",
        }
    ],
    model="gpt-3.5-turbo",
)