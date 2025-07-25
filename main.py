import os
import sys
from dotenv import load_dotenv
from google import genai
from google.genai import types

from functions.get_files_info import schema_get_files_info

# PROMPT = "Why is Boot.dev such a great place to learn backend development? Use one paragraph maximum."

def main():
    cmd_args = sys.argv
    arg_count = len(cmd_args)
    if arg_count <= 1:
        print("Program needs prompt as an argument! Exit immediately!")
        sys.exit(1)
    verbose = True  if arg_count == 3 and cmd_args[2] == "--verbose" else False       
    
    
    messages = [
        types.Content(role="user", parts=[types.Part(text=cmd_args[1])]),
    ]

    load_dotenv()
    api_key = os.environ.get("GEMINI_API_KEY")
    client = genai.Client(api_key=api_key)
    available_functions = types.Tool(
    function_declarations=[
        schema_get_files_info,
    ])
    system_prompt = """
    You are a helpful AI coding agent.

    When a user asks a question or makes a request, make a function call plan. You can perform the following operations:

    - List files and directories

    All paths you provide should be relative to the working directory. You do not need to specify the working directory in your function calls as it is automatically injected for security reasons.
    """
    conf = types.GenerateContentConfig(tools=[available_functions], system_instruction=system_prompt)
    response = client.models.generate_content(
        model='gemini-2.0-flash-001', contents=messages, config=conf,
    )

    if verbose:
        print(f"User prompt: {cmd_args[1]}\n")
    if response.function_calls:
        for function_call_part in response.function_calls:
            print(f"Calling function: {function_call_part.name}({function_call_part.args})")
    else:
        print(response.text)
    if verbose:
        print(f"Prompt tokens: {response.usage_metadata.prompt_token_count}")
        print(f"Response tokens: {response.usage_metadata.candidates_token_count}\n")

main()