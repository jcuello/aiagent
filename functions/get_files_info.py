import os
import google
from google.genai import types

def get_files_info(directory="."):
  result = ""
  working_directory="/home/jose/workspace/bootdev/aiagent/calculator"
  try:
    path = os.path.abspath(os.path.join(working_directory, directory))

    if working_directory not in path:
      return f'Error: Cannot list "{directory}" as it is outside the permitted working directory'
    
    if os.path.isfile(path):
      return f'Error: "{directory}" is not a directory'

    ls_results = os.listdir(path)

    def format_ls_results(file_or_dir):
      full_path = f"{path}/{file_or_dir}"
      return f"- {file_or_dir}: file_size={os.path.getsize(full_path)} bytes, is_dir={os.path.isdir(full_path)}"
    
    formatted_results = list(map(format_ls_results, ls_results))
    result = "\n".join(formatted_results)
  except Exception as e:
    return f"Error: {e}"
  
  return result

schema_get_files_info = types.FunctionDeclaration(
    name="get_files_info",
    description="Lists files in the specified directory along with their sizes, constrained to the working directory.",
    parameters=types.Schema(
        type=types.Type.OBJECT,
        properties={
            "directory": types.Schema(
                type=types.Type.STRING,
                description="The directory to list files from, relative to the working directory. If not provided, lists files in the working directory itself.",
            ),
        },
    ),
)

available_functions = types.Tool(
  function_declarations=[
    schema_get_files_info,
  ]
)