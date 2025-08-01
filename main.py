import os
import sys
from dotenv import load_dotenv
from google import genai
from google.genai import types

from functions.get_files_info import schema_get_files_info
from functions.get_file_content import schema_get_file_content
from functions.write_file import schema_write_file
from functions.run_python import schema_run_python_file
from functions.call_function import call_function

# PROMPT = "Why is Boot.dev such a great place to learn backend development? Use one paragraph maximum."

def main():
    cmd_args = sys.argv
    arg_count = len(cmd_args)
    if arg_count <= 1:
        print("Program needs prompt as an argument! Exit immediately!")
        sys.exit(1)
    verbose = True  if arg_count == 3 and cmd_args[2] == "--verbose" else False       
    
    if verbose:
        print(f"User prompt: {cmd_args[1]}\n")
    
    messages = [
        types.Content(role="user", parts=[types.Part(text=cmd_args[1])]),
    ]

    load_dotenv()
    api_key = os.environ.get("GEMINI_API_KEY")
    client = genai.Client(api_key=api_key)
    available_functions = types.Tool(
        function_declarations=[
            schema_get_files_info,
            schema_get_file_content,
            schema_write_file,
            schema_run_python_file,
        ]
    )
    system_prompt = """
    You are a helpful AI coding agent.

    When a user asks a question or makes a request, make a function call plan. 
    You can perform the following operations:

    - List files and directories
    - Read file contents
    - Execute Python files with optional arguments
    - Write or overwrite files

    All paths you provide should be relative to the working directory, which contains calculator app source code.
    You do not need to specify the working directory in your function calls as it is automatically injected for security reasons.
    """
    conf = types.GenerateContentConfig(tools=[available_functions], system_instruction=system_prompt)
    for i in range(20):
        try:
            response = client.models.generate_content(
                model='gemini-2.0-flash-001', contents=messages, config=conf,
            )            
            if response.candidates:
                for candidate in response.candidates:
                    messages.append(candidate.content)
            if response.function_calls:
                for function_call_part in response.function_calls:
                    function_call_result = call_function(function_call_part, verbose)
                    function_response = function_call_result.parts[0].function_response.response
                    if not function_response:
                        raise Exception("Fatal ERROR! No result from called function.")
                    if verbose:
                        print(f"-> {function_response}")
                    messages.append(types.Content(role="user", parts=[types.Part(text=function_response['result'])]))
            else:
                print(response.text)
                break
            if verbose:
                print(f"Prompt tokens: {response.usage_metadata.prompt_token_count}")
                print(f"Response tokens: {response.usage_metadata.candidates_token_count}\n")
        except Exception as e:
            print(f"Error: {e}")

main()