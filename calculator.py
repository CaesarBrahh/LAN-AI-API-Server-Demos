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
            "system": "You are a calculator. You will be given an equation. Respond with ONLY the ANSWER. ONLY RETURN THE NUMBER!",
            "prompt": equation,
            "stream": False
        }
    )

    # output
    data = response.json()
    print(f"Answer: {data['response']}")
    
if __name__=="__main__":
    main()
