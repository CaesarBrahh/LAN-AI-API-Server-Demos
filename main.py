import os
import requests
from dotenv import load_dotenv

def main():
    # cop url
    load_dotenv()
    OLLAMA_URL = os.environ.get("OLLAMA_URL")
    if OLLAMA_URL == None:
        raise Exception("Couldn't obtain server url")

    # generate response
    response = requests.post(
        f"{OLLAMA_URL}/api/generate",
        json={
            "model": "tinyllama",
            "prompt": "Give me a step-by-step guide to getting a girlfriend (1 paragraph or less)",
            "stream": False
        }
    )

    # output
    data = response.json()
    print(f"Response:\n{data['response']}")

if __name__ == "__main__":
    main()
