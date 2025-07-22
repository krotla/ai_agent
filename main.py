import os
import sys
from dotenv import load_dotenv
from google import genai
from google.genai import types

# PROMPT = "Why is Boot.dev such a great place to learn backend development? Use one paragraph maximum."

def main():
    cmd_args = sys.argv
    arg_count = len(cmd_args)
    if arg_count <= 1:
        print("Program needs prompt as an argument! Exit immediately!")
        sys.exit(1)
    verbose = True  if arg_count == 3 and cmd_args[2] == "--verbose" else False       

    load_dotenv()
    api_key = os.environ.get("GEMINI_API_KEY")

    client = genai.Client(api_key=api_key)

    messages = [
        types.Content(role="user", parts=[types.Part(text=cmd_args[1])]),
    ]

    response = client.models.generate_content(
        model='gemini-2.0-flash-001', contents=messages
    )
    if verbose:
        print(f"User prompt: {cmd_args[1]}\n")
    print(response.text)
    if verbose:
        print(f"Prompt tokens: {response.usage_metadata.prompt_token_count}")
        print(f"Response tokens: {response.usage_metadata.candidates_token_count}\n")

main()