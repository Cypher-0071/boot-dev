import os
def write_file(working_directory: str, file_path: str, content: str) -> str:
    try:
        w_dir_abs = os.path.abspath(working_directory)
        path =  os.path.normpath(os.path.join(w_dir_abs, file_path))
        valid_target_dir = os.path.commonpath([w_dir_abs, path]) == w_dir_abs
        
        if not valid_target_dir:
            return f'Error: Cannot write to "{file_path}" as it is outside the permitted working directory'
        if os.path.isdir(path):
            return f'Error: Cannot write to "{file_path}" as it is a directory'
        
        os.makedirs(os.path.dirname(path), exist_ok=True)
        
        with open(path, "w", encoding="utf-8") as f:
            f.write(content)
            
        return f'Successfully wrote to "{file_path}" ({len(content)} characters written)'

    except Exception as e:
        return f"Error: {e}"