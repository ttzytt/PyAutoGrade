import os 
from pathlib import Path
import yaml
import re
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
        if parts[i] == old:
            parts[i] = new
            break
    return os.path.join(*parts)

def get_abs_norm_path_str(path : str) -> str:
    return str(Path(path).resolve())
def get_norm_path_str(path : str) -> str:
    return str(Path(path))
def remove_first_dot_if_preceding_spaces(s):
    parts = s.split('.', 1)  # Split the string into two parts at the first dot
    if len(parts) == 2 and (not parts[0] or parts[0].isspace()):  # Check if the first part contains only spaces or nothing
        return parts[0].rstrip() + parts[1]  # If so, remove trailing spaces and concatenate with the second part
    return s

class CfgFileRelated: 
    def _get_abs_path_in_cfg(self, path: str) -> str:
        # get the absolute path of `path` in the cfg file
        # if `path` is not a relative path, return `path`
        if not os.path.isabs(path):
            return os.path.join(self.cfg_folder_abs_path, path)
        else:
            return path
    def __init__(self, cfg_path: str = './config.yml') -> None:
        self.cfg = yaml.load(open(cfg_path, 'r'), Loader=yaml.FullLoader)
        self.cfg_abspath = os.path.abspath(cfg_path)
        self.cfg_folder_abs_path = os.path.join(
            *Path(self.cfg_abspath).parts[:-1])
        self.tested_code_abs_path = self._get_abs_path_in_cfg(
            self.cfg['tested_code_path'])
        self.tested_code_rel_path = self.cfg['tested_code_path']
        self.test_case_abs_path = self._get_abs_path_in_cfg(
            self.cfg['test_case_path'])
        self.test_case_rel_path = self.cfg['test_case_path']
        self.temp_files_abs_path = self._get_abs_path_in_cfg(
            self.cfg['temp_files_path']
        )
        self.temp_files_rel_path = self.cfg['temp_files_path']
        self.output_abs_path = self._get_abs_path_in_cfg(
            self.cfg['output_path']
        )
        self.output_rel_path = self.cfg['output_path']


        student_re_list = self.cfg['students_list'] # all regular expressions
        student_list = []

        # Iterate over each regular expression
        for re_str in student_re_list:
            # Compile the regular expression
            pattern = re.compile(re_str)
            
            # Iterate over all files in the directory
            for file_or_folder in Path(self.tested_code_abs_path).glob('*'):
                # Check if the file name matches the regular expression
                print(f"Matching {file_or_folder.name} with {re_str}")
                if pattern.fullmatch(file_or_folder.name):
                    print("Matched!")
                    student_list.append(file_or_folder.name)

        self.student_list = student_list
        print(f"Student list: {self.student_list}")
        self.problem_list = self.cfg['problems_list']