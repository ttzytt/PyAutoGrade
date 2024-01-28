import os 
from pathlib import Path
import yaml
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
