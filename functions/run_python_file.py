import os
import subprocess

def run_python_file(working_directory, file_path, args=[]):
    try:
      abs_path = os.path.abspath(os.path.join(working_directory, file_path))

      if working_directory not in abs_path:
        return f'Error: Cannot execute "{file_path}" as it is outside the permitted working directory'
      
      if not os.path.exists(abs_path):
        return f'Error: File "{file_path}" not found.'
      
      base_name, file_extension = os.path.splitext(abs_path)
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


