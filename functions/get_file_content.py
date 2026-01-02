import os
import config
from google.genai import types

def get_file_content(working_directory, file_path):
  try:
    path = os.path.abspath(os.path.join(working_directory, file_path))    

    if working_directory not in path:
      return f'Error: Cannot read "{file_path}" as it is outside the permitted working directory'
    
    if not os.path.isfile(path):
      f'Error: File not found or is not a regular file: "{file_path}"'

    with open(path) as file:
      contents = file.read()
      if len(contents) > config.CHARACTER_LIMIT_COUNT:
        contents = contents[:config.CHARACTER_LIMIT_COUNT] + f'[...File "{file_path}" truncated at {config.CHARACTER_LIMIT_COUNT} characters]'

    return contents
  except Exception as e:
    return f"Error: {e}"
  
schema_get_file_content = types.FunctionDeclaration(
    name="get_file_content",
    description="Reads file contents specified by the file path.",
    parameters=types.Schema(
        type=types.Type.OBJECT,
        properties={
            "file_path": types.Schema(
                type=types.Type.STRING,
                description="The file path of the file to read.",
            ),
            "file_path": types.Schema(
                type=types.Type.STRING,
                description="The file path of the file to read.",
            ),
        },
    ),
)

available_functions = types.Tool(
  function_declarations=[
    schema_get_file_content,
  ]
)