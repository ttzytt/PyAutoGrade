#!/usr/bin/env python3
import yaml
import os
from pathlib import Path
from helpers import *
import datetime
import shutil
from tqdm import tqdm
import argparse
class FileManager(CfgFileRelated):
    def __init__(self, cfg_path : str = './config.yml') -> None:
        super().__init__(cfg_path)  
    
    def get_all_by_problem(self, *p_or_folder_names : str):
        """ 
            Move all students' solution for problem/folder name into `temp_files_path`
            After this operation, the `temp_files_path` will be like this:
            
            temp_files_path
                - problem1_2023-10-25 14#57#13.377097
                    - stu1.py
                    - stu2.py
                    - stu3.py
                    ...
                - problem2_2023-10-25 14#57#13.377097
                    - stu1.py 
                    ... 
                ...
        """
        pbar_problems = tqdm(p_or_folder_names)
        for pfname in pbar_problems:
            pbar_problems.set_description(f"Copying file/folder: {pfname}")
            timestr =  str(datetime.datetime.now())
            # replace : with #, because : is not allowed to use in file name
            timestr = timestr.replace(':', '#')
            os.mkdir(os.path.join(self.temp_files_abs_path, pfname + '_' + timestr))
            for stu in tqdm(self.cfg['students_list']):
                orig_solution_file_path = os.path.join(self.tested_code_abs_path, stu, pfname + '.py')
                if os.path.exists(orig_solution_file_path):
                    solution_file = open(orig_solution_file_path, 'r')
                    dest_solution_file_path = os.path.join(self.temp_files_abs_path, pfname + '_' + timestr, stu + '.py')
                    if os.path.isdir(orig_solution_file_path):
                        shutil.copytree(orig_solution_file_path, dest_solution_file_path)
                    else: 
                        shutil.copyfile(orig_solution_file_path, dest_solution_file_path)   
                else: 
                    # create a file named: stu-no-solution.py
                    dest_solution_file_path = os.path.join(self.temp_files_abs_path, pfname + '_' + timestr, stu + ' [no solution found].py')
                    dest_solution_file = open(dest_solution_file_path, 'w')
                    dest_solution_file.close()
                    
    def clear_cache(self):
        """ 
            Clear all files in `temp_files_path`
        """
        shutil.rmtree(self.temp_files_abs_path)
        os.mkdir(self.temp_files_abs_path)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Copy all students\' file or folder into a folder in `temp_files_path`')
    # use --cfg / -c to specify the path to the config file
    # use --file_folder / -ff to specify the file ors folder to copy
    parser.add_argument('--cfg', '-c', type=str, default='./config.yml', help='path to the config file')
    parser.add_argument('--move_file_folder', '-mf', type=str, nargs='+', help='file or folder to copy')
    parser.add_argument('--clear_cache', '-cc', action='store_true', help='clear all files in `temp_files_path`')
    args = parser.parse_args()
    fm = FileManager(args.cfg)
    if args.clear_cache:
        fm.clear_cache()
    if args.move_file_folder:
        fm.get_all_by_problem(*args.move_file_folder)