import os
from config import TRUNCATE_CHARACTER_LIMIT


def write_file(working_directory, file_path, content):
    abs_working_dir = os.path.abspath(working_directory)
    abs_file_path = os.path.abspath(os.path.join(abs_working_dir, file_path))
    if not abs_file_path.startswith(abs_working_dir):
        return f'Error: Cannot write to "{file_path}" as it is outside the permitted working directory'

    try:
        file_directory_path = os.path.dirname(abs_file_path)
        if not os.path.exists(file_directory_path):
            os.makedirs(file_directory_path)   
        with open(abs_file_path, "w") as f:
            f.write(content)                
        return f'Successfully wrote to "{file_path}" ({len(content)} characters written)'
    
    except Exception as e:
        return f"Error: {e}"