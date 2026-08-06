import os
def get_files_info(working_directory: str, directory: str = ".") -> str:
    try:
        w_dir_abs = os.path.abspath(working_directory)
        target_dir = os.path.normpath(os.path.join(w_dir_abs, directory))
        valid_target_dir = os.path.commonpath([w_dir_abs, target_dir]) == w_dir_abs

        if not valid_target_dir:
            return f'Error: Cannot list "{directory}" as it is outside the permitted working directory'

        if not os.path.isdir(target_dir):
            return f'Error: "{directory}" is not a directory'
        result = []
        for f in os.listdir(target_dir):
            path = os.path.join(target_dir, f)
            f_size = os.path.getsize(path)
            is_dir = os.path.isdir(path)
            result.append(f"{f}: file_size={f_size} bytes, is_dir={is_dir}")
        return f"Result for {target_dir} directory:\n{result}"
    except Exception as e:
        return f"Error: {e}"

schema_get_files_info = {
    "type": "function",
    "function": {
        "name": "get_files_info",
        "description": "Lists files in a specified directory relative to the working directory, providing file size and directory status",
        "parameters": {
            "type": "object",
            "properties": {
                "directory": {
                    "type": "string",
                    "description": "Directory path to list files from, relative to the working directory (default is the working directory itself)",
                },
            },
        },
    },
}