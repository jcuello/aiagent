import os
import sys
from typing import Any
import config
from dotenv import load_dotenv

load_dotenv()
api_key = os.environ.get("GEMINI_API_KEY")

from google import genai
from google.genai import types
import functions.get_files_info
import functions.get_file_content
import functions.write_file
import functions.run_python_file

client = genai.Client(api_key=api_key)

func_map = {
    "get_files_info": functions.get_files_info.get_files_info,
    "get_file_content": functions.get_file_content.get_file_content,
    "write_file": functions.write_file.write_file,
    "run_python_file": functions.run_python_file.run_python_file
}

def main():
    verbose = False
    arg_len = len(sys.argv)
    if arg_len == 1:
        print("Prompt argument required.")
        exit(1)

    user_prompt = sys.argv[1]
    messages = [
        types.Content(role="user", parts=[types.Part(text=user_prompt)])
    ]

    response = client.models.generate_content(
        model='gemini-2.5-flash',
        contents=messages,
        config=types.GenerateContentConfig(
            tools=[
                functions.get_files_info.available_functions,
                functions.get_file_content.available_functions,
                functions.write_file.available_functions,
                functions.run_python_file.available_functions,
            ],
            system_instruction=config.SYSTEM_PROMPT,
        )
    )
    
    if "--verbose" in sys.argv:
        verbose = True     
        print(f"User prompt: {user_prompt}")
        print(f"Prompt tokens: {response.usage_metadata.prompt_token_count}")
        print(f"Response tokens: {response.usage_metadata.candidates_token_count}")

    function_responses: list[types.Part] = []
    if response.function_calls != None:
        function_call = response.function_calls[0]
        function_call_result = call_function(function_call, verbose)

        if function_call_result.parts == None or len(function_call_result.parts) == 0:
            raise Exception("function_call_result.parts is empty.")
        
        func_response = function_call_result.parts[0].function_response
        if func_response == None:
            raise Exception("parts[0].function_response is empty.")
        
        function_responses.append(function_call_result.parts[0])
        if verbose:
            print(f"-> {func_response.response}")
        
    else:
        # if no function was called, Gemini will give a text reply such as an
        # error or confirmation e.g. "I can show you the files in the root directory. Would you like me to do that?"
        print(response.text)

def call_function(function_call:types.FunctionCall, verbose=False):
    function_name = function_call.name or ""
    function_args = function_call.args
    if verbose:
        print(f"Calling function: {function_name}({function_args})")
    else:
        print(f" - Calling function: {function_name}")

    if function_name not in func_map:
        return types.Content(
            role="tool",
            parts=[
                types.Part.from_function_response(
                    name=function_name,
                    response={"error": f"Unknown function: {function_name}"},
                )
            ],
        )
    args = dict(function_args) if function_args else {}
    args["working_directory"] = "calculator"

    function_result = func_map[function_name](**args)
    return types.Content(
        role="tool",
        parts=[
            types.Part.from_function_response(
                name=function_name,
                response={"result": function_result},
            )
        ],
    )

if __name__ == "__main__":
    main()
