import os
import subprocess
from google.genai import types

def run_python_file(working_directory, file_path, args=[]):
    try:
      abs_path = os.path.abspath(os.path.join(working_directory, file_path))

      if working_directory not in abs_path:
        return f'Error: Cannot execute "{file_path}" as it is outside the permitted working directory'
      
      if not os.path.exists(abs_path):
        return f'Error: File "{file_path}" not found.'
      
      _, file_extension = os.path.splitext(abs_path)
      if file_extension.lower() != '.py':
        return f'Error: "{file_path}" is not a Python file.'
      
      completed_process = subprocess.run(
        timeout=30, capture_output=True,cwd=os.path.dirname(abs_path),
        args=["python", file_path, *args], text=True)
      
      if completed_process.returncode != 0:
        return f'Process exited with code {completed_process.returncode}'
      
      if completed_process.stdout == None and completed_process.stderr == None:
        return 'No output produced.'
      
      return f'STDOUT: {completed_process.stdout}\nSTDERR: {completed_process.stderr}'
    except Exception as e:
      return f"Error: executing Python file: {e}"

schema_run_python_file = types.FunctionDeclaration(
    name="run_python_file",
    description="Runs python file specified by the file path.",
    parameters=types.Schema(
        type=types.Type.OBJECT,
        properties={
            "file_path": types.Schema(
                type=types.Type.STRING,
                description="The file path of the python file to run.",
            ),
            "args": types.Schema(
                type=types.Type.ARRAY,
                description="The optional list of arguments to pass to the python file.",
                items=types.Schema(type=types.Type.STRING)
            ),     
        },
    ),
)

available_functions = types.Tool(
  function_declarations=[
    schema_run_python_file,
  ]
)
