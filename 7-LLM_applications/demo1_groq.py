import os
from openai import OpenAI
import requests
from dotenv import load_dotenv  # Load environment variables from .env file

load_dotenv()  # Load environment variables from .env file
api_key = os.getenv("GROQ_API_KEY")  # Get the API key from environment variables

if not api_key:
    print("❌ No API key found!")
    print("   Create a .env file with: GROQ_API_KEY=your_key_here")
    print("   Get a free key at: https://console.groq.com/keys")
    exit(1)


client = OpenAI(
    api_key=api_key,
    base_url="https://api.groq.com/openai/v1"
)

models = client.models.list()

for model in models.data:
    print(model.id)

print("=" * 60)

print("  DEMO 1 — Your First LLM API Call")
###
print("  Model: qwen/qwen3.8-27b, allam-2-7b (qwen and Meta's open-source model, hosted on Groq)")
print("=" * 60)
print()

try:
    response = client.chat.completions.create(
        model="qwen/qwen3.8-27b",   # Meta's LLaMA 3.3 — open source! # allam-2-7b
        messages=[
            {
                "role": "system",           # System message = instructions to the AI
                "content": "You are a friendly AI assistant. Keep answers short and clear."
            },
            {
                "role": "user",             # User message = the actual question
                "content": "Explain what a Large Language Model is in 2 simple sentences."
            }
        ],
        temperature=0.7,    # 0 = very consistent, 1 = more creative
        max_tokens=200      # Maximum words in the response
    )

    print("🧠 AI Response:")
    # best-effort: print the usual field, otherwise print whole response for debugging
    try:
        print(response.choices[0].message.content)
    except Exception:
        print(response)
except Exception as e:
    print("API call failed:", type(e).__name__, str(e))
    import traceback
    traceback.print_exc()
    
