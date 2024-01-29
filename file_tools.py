import os

from langchain.tools import tool


class FileTools:

    @tool("Write File with content")
    def write_file(data: str):
        """Useful to write a file to a given path with a given content. 
           The input to this tool should be a pipe (|) separated text 
           of length two, representing the full path of the file, 
           including the ./lore/, and the written content you want to write to it.
        """
        try:
            path, content = data.split("|")
            path = path.replace("\n", "").replace(" ", "").replace("`", "")
            if not path.startswith("./lore"):
                path = f"./lore/{path}"
            with open(path, "w") as f:
                f.write(content)
            return f"File written to {path}."
        except Exception:
            return "Error with the input format for the tool."

    @tool("Create files")
    def create_file(path:str):
      """usefull for creating files in the local disk"""
      try:
        folder_name, file_name = os.path.split(path)
      # Create the folder
        os.makedirs(folder_name, exist_ok=True)

      # Path to the new file within the folder
        file_path = os.path.join(folder_name, file_name)
        with open(file_path, "w") as file:
          pass
        print(f"Folder file path {folder_name}+'/'+{file_name} created successfully")
        return file_path
      except Exception:
        return "Error creating filepath"
