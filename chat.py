'''
TODO:
- aesthetics
'''
import os
import sys
import json
import requests
from dotenv import load_dotenv

def main():
    # cop url
    load_dotenv()
    OLLAMA_URL = os.environ.get("OLLAMA_URL")
    if OLLAMA_URL == None:
        raise Exception("Couldn't obtain server url")

    # initialize messages
    messages = []
    
    while True:
        # collect the user's prompt
        user_prompt = input("User: ")

        # exit chat user types 'exit'
        if user_prompt == "exit":
            sys.exit("Chat ended.")

        # add user prompt to messages
        messages.append({"role": "user", "content": user_prompt})

        # send an api request to llama
        response = requests.post(
            f"{OLLAMA_URL}/api/chat",
            json={
                "model": "tinyllama",
                "messages": messages,
                "stream": True,
            },
            stream=True,
        )

        # initialize the final assistant message
        assistant_response = ""

        # print space and the assistant label
        print()
        print("Assistant: ", end="", flush=True)

        # iterate through streamlined chunks
        for line in response.iter_lines():
            # skip empty lines
            if not line:
                continue
            
            # convert json into python dictionary
            chunk = json.loads(line)
            
            # break out of loop if final chunk is sent
            if chunk.get("done"):
                break

            # extract generated token text and append to assistant_response
            content = chunk["message"]["content"]
            assistant_response += content

            # print token live
            print(content, end="", flush=True)

        # finish with 2 new lines
        print()
        print()

        # append assistant response to messages array
        messages.append({"role": "assistant", "content": assistant_response})

if __name__=="__main__":
    main()
