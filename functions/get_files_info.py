import os

def get_files_info(working_directory, directory="."):     
    abs_working_dir = os.path.abspath(working_directory)
    full_path = os.path.abspath(os.path.join(abs_working_dir, directory))
    if not full_path.startswith(abs_working_dir):
        return f'Error: Cannot list "{directory}" as it is outside the permitted working directory'
    if not os.path.isdir(full_path):
        return f'Error: "{directory}" is not a directory'
    try:
        files_info = []
        dir_content = os.listdir(full_path)
        dir_content.sort()
        for file_name in dir_content:
            file_path = os.path.join(full_path, file_name)
            is_dir = os.path.isdir(file_path)                
            file_size = os.path.getsize(file_path)         
            files_info.append(f" - {file_name}: file_size={file_size or 0} bytes, is_dir={is_dir}")
        return "\n".join(files_info)
    except Exception as e:
        return f"Error: {e}"

