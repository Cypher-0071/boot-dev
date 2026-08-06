import os
from dotenv import load_dotenv
from openai import OpenAI
import argparse
import sys
from prompts import system_prompt
from call_functions import available_functions
from functions.call_function import call_function
import json

load_dotenv()
api_key = os.environ.get("OPENROUTER_API_KEY")

parser = argparse.ArgumentParser(description="Chatbot")
parser.add_argument("user_prompt", type=str, help="User prompt")
parser.add_argument("--verbose", action="store_true", help= "Enable verbose output")
args = parser.parse_args()

client = OpenAI(
    base_url="https://openrouter.ai/api/v1",
    api_key=api_key,
)

model = 'openrouter/free'

messages = [
    {
        "role": "system",
        "content": system_prompt
    },
    {
        "role": "user",
        "content": args.user_prompt,
    }
]

max_iterations = 20

for _ in range(max_iterations):
    response = client.chat.completions.create(messages=messages, model=model, temperature=0, tools=available_functions)
    if response.usage is not None and args.verbose:
        print(f"User prompt: {messages[1]['content']}")
        print(f"Prompt tokens: {response.usage.prompt_tokens}")
        print(f"Response tokens: {response.usage.completion_tokens}")

    message = response.choices[0].message
    messages.append(message)

    if message.tool_calls:
        for tool_call in message.tool_calls:
            result_message = call_function(tool_call, verbose=args.verbose)
            if not result_message.get("content"):
                raise Exception(f"Tool call {tool_call.function.name} returned empty content")
            if args.verbose:
                print(f"-> {result_message['content']}")
            messages.append(result_message)
    else:
        print(message.content)
        break
else:
    print("Error: Maximum iterations reached without receiving a final response.")
    sys.exit(1)
