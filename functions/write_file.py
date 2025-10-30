import os

def write_file(working_directory, file_path, content):
  try:
    abs_path = os.path.abspath(os.path.join(working_directory, file_path))

    if working_directory not in abs_path:
      return f'Error: Cannot write to "{file_path}" as it is outside the permitted working directory'
    
    dir_path = os.path.dirname(abs_path)
    if not os.path.exists(dir_path):
      os.makedirs(dir_path)

    with open(abs_path, "w") as f:
      f.write(content)
      return f'Successfully wrote to "{file_path}" ({len(content)} characters written)'

  except Exception as e:
    return f'Error: {e}'