#!/usr/bin/env python3
from typing import Callable
import yaml
import os
from pathlib import Path
from helpers import *
import datetime
import shutil
from tqdm import tqdm
import argparse
import random
import pathlib
import re

class FileManager(CfgFileRelated):
    def __init__(self, cfg_path : str = './config.yml') -> None:
        super().__init__(cfg_path)  
    
    def get_timestr(self) -> str:
        return str(datetime.datetime.now()).replace(':', '#')

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
        timestr = self.get_timestr()
        isfile_pfname_pbar = tqdm(zip(isfiles, p_or_folder_names))
        for isfile, pfname in isfile_pfname_pbar:
            isfile_pfname_pbar.set_description(f"Copying file/folder: {pfname}")
            # replace : with #, because : is not allowed to use in file name
            
            # some file_name passed here might be /folder/file.py
            # so replace / with other stuff
            # also put time into pfname 
            if isfile and pfname.find('.') != -1:
                extension_name = "." + pfname.split('.')[-1]
            else: 
                extension_name = ''
            destination_pfname = pfname.replace('/', '$') + '_' + timestr + extension_name # destination problem/folder name
            destination_pfname = remove_first_dot_if_preceding_spaces(destination_pfname)
            os.mkdir(os.path.join(self.temp_files_abs_path, destination_pfname))
            for stu in tqdm(self.student_list):
                student_pf_path = os.path.join(self.tested_code_abs_path, stu, pfname)
                if os.path.exists(student_pf_path):
                    dest_solution_file_path = os.path.join(self.temp_files_abs_path, destination_pfname, stu + extension_name)
                    if isfile:
                        shutil.copyfile(student_pf_path, dest_solution_file_path)   
                    else: 
                        shutil.copytree(student_pf_path, dest_solution_file_path)
                else: 
                    # create a file named: stu-no-solution.py
                    dest_solution_file_path = os.path.join(self.temp_files_abs_path, destination_pfname, stu + ' [no solution found]' + extension_name)
                    dest_solution_file = open(dest_solution_file_path, 'w')
                    dest_solution_file.close()
                    
    def clear_cache(self):
        """ 
            Clear all files in `temp_files_path`
        """
        shutil.rmtree(self.temp_files_abs_path)
        os.mkdir(self.temp_files_abs_path)
    
    def obfuscate_tested_codes(self, hash_func : Callable[[str], int] | None = adding_hash_func):
        """
            This function is designed to meet the compliance rule of the school. 
            Specifically, it will replace the name of the student in the input folder 
            with a random number. Then it will delet    e all comments in the solution file,
            as in some cases, students indicate their name in comments.
        
        """
        stus : list[str] = self.student_list
        stus_to_num : dict[str, int] = {}
        random.shuffle(stus)
        if hash_func is None:
            for num, stu in enumerate(stus):
                stus_to_num[stu] = num
        else: 
            for stu in stus:
                stus_to_num[stu] = hash_func(stu)
        
        def remove_comments(program : str) -> str:
            # Remove single-line comments
            program = re.sub(r'(\'[^\']*\'|\"[^\"]*\")|(#.*?\n)', lambda m: m.group(1) if m.group(1) else '\n', program)
            # Remove multi-line comments
            # program = re.sub(r'""".*?"""', '', program, flags=re.DOTALL)
            # program = re.sub(r"'''.*?'''", '', program, flags=re.DOTALL)
            return program
        
        copy_folder_name = "obfuscated_tested_codes [copied at {}]".format(self.get_timestr())

        for stu in stus: 
            stu_path = pathlib.Path(os.path.join(self.tested_code_abs_path, stu))
            stu_num = stus_to_num[stu]
            all_pyfiles = list(stu_path.rglob("*.py"))
            if len(all_pyfiles) == 0:
                # no file found for this student
                # but still open a folder for this student
                os.makedirs(os.path.join(self.cfg_folder_abs_path, self.temp_files_rel_path, copy_folder_name, str(stu_num)))
            for pyfile_path in all_pyfiles:
                with open(pyfile_path, 'r') as f:
                    program = f.read()
                program = remove_comments(program)
                # replace the name of the student with a random number in pyfile_path
                # also make sure that the new file is in the cache
                
                pyfile_name = str(pyfile_path).replace(get_abs_norm_path_str(self.tested_code_abs_path), '').replace(stu, "", 1)
                # remove all / at the beginning of the path
                while pyfile_name[0] == '/':
                    pyfile_name = pyfile_name[1:]
                no_name_path_with_file = os.path.join(self.cfg_folder_abs_path, self.temp_files_rel_path, copy_folder_name, str(stu_num), pyfile_name)
                # create the folder if not exists
                # remove the last part to make it become a folder
                no_name_path = os.path.join(*Path(no_name_path_with_file).parts[:-1])
                if not os.path.exists(no_name_path):
                    os.makedirs(no_name_path)
                with open(no_name_path_with_file, 'w') as f:
                    f.write(program)
            
                

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Copy all students\' file or folder into a folder in `temp_files_path`')
    # use --cfg / -c to specify the path to the config file
    # use --file_folder / -ff to specify the file ors folder to copy
    parser.add_argument('--cfg', '-c', type=str, default='./config.yml', help='path to the config file')
    parser.add_argument('--move_files', '-mf', type=str, nargs='+', help='move files to `temp_files_path`')
    parser.add_argument('--move_directories', '-md', type=str, nargs='+', help='move folders to `temp_files_path`')
    parser.add_argument('--clear_cache', '-cc', action='store_true', help='clear all files in `temp_files_path`')
    parser.add_argument('--obfuscate_tested_codes', '-oc', action='store_true', help='obfuscate all tested codes')
    args = parser.parse_args()
    fm = FileManager(args.cfg)
    if args.clear_cache:
        fm.clear_cache()
    if args.move_files:
        fm.get_all_by_problem([True] * len(args.move_files), *args.move_files)
    if args.move_directories:
        fm.get_all_by_problem([False] * len(args.move_directories), *args.move_directories)
    if args.obfuscate_tested_codes:
        fm.obfuscate_tested_codes()