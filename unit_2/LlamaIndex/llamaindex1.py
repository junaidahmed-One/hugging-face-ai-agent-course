import os

from dotenv import load_dotenv
from llama_index.llms.openrouter import OpenRouter

load_dotenv()

openrouter_api_key = os.getenv("OPENROUTER_API_KEY")

llm = OpenRouter(
    api_key=openrouter_api_key,
    model="google/gemma-4-26b-a4b-it:free",
    temperature=0.7,
    max_tokens=100,
)

response = llm.complete("Hello, How are you?")
print(response)
