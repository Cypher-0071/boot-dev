import os
from config import limit
def get_file_content(working_directory: str, file_path: str) -> str:
    try:
        w_dir_abs = os.path.abspath(working_directory)
        path =  os.path.normpath(os.path.join(w_dir_abs, file_path))
        valid_target_dir = os.path.commonpath([w_dir_abs, path]) == w_dir_abs
        if not valid_target_dir:
            return f'Error: Cannot list "{file_path}" as it is outside the permitted working directory'
        if not os.path.isfile(path):
            return f'Error: File not found or is not a regular file: "{file_path}"'
        
        with open(path) as f:
            file_content = f.read(limit)
            if f.read(1):
                file_content += f'[...File "{file_path}" truncated at {limit} characters]'
            return file_content
        
    except Exception as e:
        return f"Error: {e}"