import os
import requests
from dotenv import load_dotenv  # Load environment variables from .env file
from ollama import generate

load_dotenv()
# Ollama local endpoint (default) and model (default to gemma4)
OLLAMA_URL = os.getenv("OLLAMA_URL", "http://localhost:11434/api/generate")
OLLAMA_MODEL = os.getenv("OLLAMA_MODEL", "gemma4")


print("=" * 60)
print("  DEMO 1 — Your First LLM API Call")
print("  Model: (OLLAMA) " + OLLAMA_MODEL)
print("=" * 60)
print()
prompt = (
    "You are a friendly AI assistant. Keep answers short and clear.\n\n"
    "Explain what a Large Language Model is in 2 simple sentences."
)

print(f"Calling Ollama at {OLLAMA_URL} with model {OLLAMA_MODEL}...")
try:
    resp = requests.post(
        OLLAMA_URL,
        json={
            "model": OLLAMA_MODEL,
            "prompt": prompt,
            "temperature": 0.7,
            "max_tokens": 200,
            "stream": False,
        },
        timeout=30,
    )

    if resp.status_code == 200:
        print("🧠 AI Response:")
        # try JSON then fallback to plain text
        try:
            print(resp.json().get("response", "").strip())
        except Exception:
            print(resp.text)
    else:
        print(f"Request failed: {resp.status_code} - {resp.text}")
except Exception as e:
    print("Request error:", type(e).__name__, str(e))
    import traceback
    traceback.print_exc()