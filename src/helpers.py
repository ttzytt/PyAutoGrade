import os 
from pathlib import Path
def replace_last_path_occurance(path : str, old : str, new : str):
    path = Path(path)
    parts = list(path.parts)
    for i in range(len(parts) - 1, -1, -1):
        # traverse reversely
        if parts[i] == old:
            parts[i] = new
            break
    return os.path.join(*parts)

def replace_first_path_occurance(path : str, old : str, new : str):
    path = Path(path)
    parts = list(path.parts)
    for i in range(len(parts)):
        # traverse reversely
        if parts[i] == old:
            parts[i] = new
            break
    return os.path.join(*parts)