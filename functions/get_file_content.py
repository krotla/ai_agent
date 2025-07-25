import os
from config import TRUNCATE_CHARACTER_LIMIT
from google.genai import types

schema_get_file_content = types.FunctionDeclaration(
    name="get_file_content",
    description=f"Lists content of specified file, constrained to the working directory. File content biger than {TRUNCATE_CHARACTER_LIMIT} characters is trunkated.",
    parameters=types.Schema(
        type=types.Type.OBJECT,
        properties={
            "file_path": types.Schema(
                type=types.Type.STRING,
                description="The file path, relative to the working directory.",
            ),
        },
    ),
)

def get_file_content(working_directory, file_path):
    abs_working_dir = os.path.abspath(working_directory)
    abs_file_path = os.path.abspath(os.path.join(abs_working_dir, file_path))
    if not abs_file_path.startswith(abs_working_dir):
        return f'Error: Cannot read "{file_path}" as it is outside the permitted working directory'
    if not os.path.isfile(abs_file_path):
        return f'Error: File not found or is not a regular file: "{file_path}"'
    try:
        with open(abs_file_path, "r") as f:
            file_content_string = f.read(TRUNCATE_CHARACTER_LIMIT + 5)
            if len(file_content_string) > TRUNCATE_CHARACTER_LIMIT:
                file_content_string = file_content_string[:TRUNCATE_CHARACTER_LIMIT] + '\n\n' \
                    + f'[...File "{file_path}" truncated at 10000 characters]'
        return file_content_string
    except Exception as e:
        return f"Error: {e}"
