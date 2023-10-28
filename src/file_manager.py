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
    
    def get_all_by_problem(self, isfiles : list[bool], *p_or_folder_names : str):
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
        timestr =  str(datetime.datetime.now())
        timestr = timestr.replace(':', '#')
        isfile_pfname_pbar = tqdm(zip(isfiles, p_or_folder_names))
        for isfile, pfname in isfile_pfname_pbar:
            isfile_pfname_pbar.set_description(f"Copying file/folder: {pfname}")
            # replace : with #, because : is not allowed to use in file name
            
            # some file_name passed here might be /folder/file.py
            # so replace / with other stuff
            # also put time into pfname 
            if isfile and pfname.find('.') != -1:
                suffix = pfname.split('.')[-1]
            else: 
                suffix = ''
            destination_pfname = pfname.replace('/', '$') + '_' + timestr + '.' + suffix # destination problem/folder name
            os.mkdir(os.path.join(self.temp_files_abs_path, destination_pfname))
            for stu in tqdm(self.cfg['students_list']):
                student_pf_path = os.path.join(self.tested_code_abs_path, stu, pfname)
                if os.path.exists(student_pf_path):
                    dest_solution_file_path = os.path.join(self.temp_files_abs_path, destination_pfname, stu + '.' + suffix)
                    if isfile:
                        shutil.copyfile(student_pf_path, dest_solution_file_path)   
                    else: 
                        shutil.copytree(student_pf_path, dest_solution_file_path)
                else: 
                    # create a file named: stu-no-solution.py
                    dest_solution_file_path = os.path.join(self.temp_files_abs_path, destination_pfname, stu + ' [no solution found]'+ '.' + suffix)
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
    parser.add_argument('--move_files', '-mf', type=str, nargs='+', help='move files to `temp_files_path`')
    parser.add_argument('--move_directories', '-md', type=str, nargs='+', help='move folders to `temp_files_path`')
    parser.add_argument('--clear_cache', '-cc', action='store_true', help='clear all files in `temp_files_path`')
    args = parser.parse_args()
    fm = FileManager(args.cfg)
    if args.clear_cache:
        fm.clear_cache()
    if args.move_files:
        fm.get_all_by_problem([True] * len(args.move_files), *args.move_files)
    if args.move_directories:
        fm.get_all_by_problem([False] * len(args.move_directories), *args.move_directories)
        