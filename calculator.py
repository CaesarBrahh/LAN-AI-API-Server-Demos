import os
import requests
from dotenv import load_dotenv

def main():
    # connect to ollama pi server
    load_dotenv()
    OLLAMA_URL = os.environ.get("OLLAMA_URL")
    if OLLAMA_URL == None:
        raise Exception("Couldn't obtain server url")

    # collect equation
    equation = input("Equation: ")

    # generate response
    response = requests.post(
        f"{OLLAMA_URL}/api/generate",
        json={
            "model": "tinyllama",
            "system": "You are a calculator. Return only the final numeric answer. No words. No explanation. No labels. Only the answer of the expression!",
            "prompt": equation,
            "stream": False,
            "options": {
                "temperature": 0,
                "top_k": 1,
                "num_predict": 3,
            }
        }
    )

    # output
    data = response.json()
    print(f"Answer: {data['response']}")
    
if __name__=="__main__":
    main()
