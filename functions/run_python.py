import os
import subprocess
from google.genai import types

schema_run_python_file = types.FunctionDeclaration(
    name="run_python_file",
    description=f"Runs the specified Python file, constrained to the working directory.",
    parameters=types.Schema(
        type=types.Type.OBJECT,
        properties={
            "file_path": types.Schema(
                type=types.Type.STRING,
                description="The file path of the Python file to run, relative to the working directory.",
            ),
            "args": types.Schema(
                type=types.Type.STRING,
                description="Arguments for the Python file to run.",
            ),
        },
    ),
)

def run_python_file(working_directory, file_path, args=[]):
    abs_working_dir = os.path.abspath(working_directory)
    abs_file_path = os.path.abspath(os.path.join(abs_working_dir, file_path))
    if not abs_file_path.startswith(abs_working_dir):
        return f'Error: Cannot execute "{file_path}" as it is outside the permitted working directory'

    try:
        if not os.path.exists(abs_file_path):
            return f'Error: File "{file_path}" not found.' 
        if not abs_file_path.endswith('.py'):
            return f'Error: "{file_path}" is not a Python file.'
        run_args = ['python3', abs_file_path]
        run_args.extend(args)
        completed_process = subprocess.run(
            run_args, timeout=30, capture_output=True, cwd=abs_working_dir)
        result = []
        if completed_process:
            result.append("STDOUT:\n" + f"{completed_process.stdout.decode()}")
            result.append("STDERR:\n" + f"{completed_process.stderr.decode()}")
            if completed_process.returncode != 0:
                result.append(f"Process exited with code {completed_process.returncode}")
            if completed_process.stdout == b'':
                result.append("No output produced.")
        return "\n".join(result)
    except Exception as e:
        return f"Error: executing Python file: {e}"