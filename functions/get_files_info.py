import os

def get_files_info(working_directory, directory="."):
  result = ""

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