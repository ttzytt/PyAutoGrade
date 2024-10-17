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
        #print("Running get_all_by_problem")
        timestr = self.get_timestr()
        isfile_pfname_pbar = tqdm(zip(isfiles, p_or_folder_names)) # Progress bar; pfname stands for problem/folder name
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

    def get_all_by_review(self, isfiles: list[bool], *p_or_folder_names: str):
        """
        Copy files or folders specified by `p_or_folder_names` for each student, 
        and organize them based on the reviewer information found in the files.
        
        Args:
            isfiles (list[bool]): List indicating whether each item in `p_or_folder_names` is a file (True) or folder (False).
            p_or_folder_names (str): Names of the files or folders to be copied.
        """
        timestr = self.get_timestr()
        isfile_pfname_pbar = tqdm(zip(isfiles, p_or_folder_names))  # Progress bar for copying files/folders
        for isfile, pfname in isfile_pfname_pbar:
            isfile_pfname_pbar.set_description(f"Copying file/folder: {pfname}")
            
            # Create a directory in temp_files_abs_path with the appropriate title
            destination_folder = os.path.join(self.temp_files_abs_path, timestr)
            if not os.path.exists(destination_folder):
                os.makedirs(destination_folder)
            
            for stu in tqdm(self.student_list):  # Iterate over each student
                print("STUDENT: ", stu)
                isfile_pfname_pbar.set_description(f"Checking Student: {stu}")
                student_pf_path = os.path.join(self.tested_code_abs_path, stu, pfname)
                print("DOES", student_pf_path, "EXIST?")
                if os.path.exists(student_pf_path):
                    print("> YES")
                    if isfile:
                        if student_pf_path.endswith('_review.py'):
                            print("> > IT ALSO ENDS WITH REVIEW")
                            self._process_file(student_pf_path, stu, pfname, timestr)
                            print("SO IM GOING TO PROCESS FILE")
                    else:

                        # Walk through the directory and process each file
                        for root, _, files in os.walk(student_pf_path):
                            for file in files:
                                if file.endswith('_review.py'):
                                    file_path = os.path.join(root, file)
                                    relative_path = os.path.relpath(file_path, student_pf_path)
                                    self._process_file(file_path, stu, relative_path, timestr)
                # else:
                #     # print("HELL NO")
                #     # Handle case where no solution is found for the student
                #     no_solution_folder = os.path.join(destination_folder, 'no_solution')
                #     if not os.path.exists(no_solution_folder):
                #         os.makedirs(no_solution_folder)
                #     dest_solution_file_path = os.path.join(no_solution_folder, stu + ' [no solution found]' + ('.' + pfname.split('.')[-1] if isfile else ''))
                #     with open(dest_solution_file_path, 'w') as dest_solution_file:
                #         dest_solution_file.close()

                # for stu in self.student_list:
                #     student_folder = os.path.join(destination_folder, stu)
                #     if not os.path.exists(student_folder):
                #         no_solution_file_path = os.path.join(destination_folder, stu + ' [no solution found]' + ('.' + pfname.split('.')[-1] if isfile else ''))
                #         with open(no_solution_file_path, 'w') as no_solution_file:
                #             no_solution_file.write(f"No solution found for {stu}")

    def _process_file(self, file_path, stu, relative_path, timestr):
        """
        Process a single file by checking for reviewer information and copying it to the appropriate folder.
        
        Args:
            file_path (str): Path to the file to be processed.
            stu (str): Name of the student.
            relative_path (str): Relative path of the file within the student's directory.
            timestr (str): Timestamp string for organizing files.
        """
        #print("PROCESSING FILE...")
        try:
            #print("TRYING TO OPEN FILE", file_path)
            with open(file_path, 'r', encoding='utf-8', errors='ignore') as file:
                print("OPENED FILE")
                content = file.read()
                # first_line = content.splitlines()[0] if content.splitlines() else "Empty file"
                # print(f"First line of {file_path}: {first_line}")
                # Check if the file contains a "Reviewed by:" line
                reviewed_by_line = next((line for line in content.splitlines() if "Reviewed by:" in line), None)
                if reviewed_by_line:
                    print("HOLY CRAP", stu, "HAS A REVIEWER!")
                    reviewer_number = reviewed_by_line.split(':')[-1].strip()
                    print("THEY ARE REVIEWED BY", reviewer_number)
                    destination_folder = os.path.join(self.temp_files_abs_path, timestr, reviewer_number)
                    print("SO OBVIOUSLY WE ARE GOING TO PUT IT IN", destination_folder)
                    if not os.path.exists(destination_folder):
                        os.makedirs(destination_folder)
                    # Create destination file path and write the content
                    dest_solution_file_path = os.path.join(destination_folder, relative_path.replace('/', '_') + '_' + stu + '.' + relative_path.split('.')[-1])
                    #print("DESTINATION FILE PATH", dest_solution_file_path)
                    with open(dest_solution_file_path, 'w', encoding='utf-8') as dest_file:
                        dest_file.write(content)
                else:
                    # Handle case where no reviewer information is found
                    #print("NO REVIEWER BOZO")
                    destination_folder = os.path.join(self.temp_files_abs_path, timestr, 'no_reviewer')
                    if not os.path.exists(destination_folder):
                        os.makedirs(destination_folder)
                    dest_solution_file_path = os.path.join(destination_folder, relative_path.replace('/', '_') + '_' + stu + '.' + relative_path.split('.')[-1])
                    shutil.copyfile(file_path, dest_solution_file_path)
        except UnicodeDecodeError as e:
            print(f"Error reading file {file_path}: {e}")
    
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
        hash_vals = set()
        if hash_func is None:
            random.shuffle(stus)
            for num, stu in enumerate(stus):
                stus_to_num[stu] = num
        else: 
            for stu in stus:
                stus_to_num[stu] = hash_func(stu)
                if stus_to_num[stu] in hash_vals:
                    stu_words = stu.split()
                    # do xor for the hash of each word 
                    extra_hash = 0
                    for word in stu_words:
                        extra_hash ^= hash_func(word)
                    stus_to_num[stu] += extra_hash
                hash_vals.add(stus_to_num[stu])
        
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
                while pyfile_name[0] == '/':
                    pyfile_name = pyfile_name[1:]
                no_name_path_with_file = os.path.join(self.cfg_folder_abs_path, self.temp_files_rel_path, copy_folder_name, str(stu_num), pyfile_name)
                no_name_path = os.path.join(*Path(no_name_path_with_file).parts[:-1])
                if not os.path.exists(no_name_path):
                    os.makedirs(no_name_path)
                with open(no_name_path_with_file, 'w') as f:
                    f.write(program)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Copy all students\' file or folder into a folder in `temp_files_path`')
    parser.add_argument('--cfg', '-c', type=str, default='./config.yml', help='path to the config file')
    parser.add_argument('--move_files', '-mf', type=str, nargs='+', help='move files to `temp_files_path`')
    parser.add_argument('--move_directories', '-md', type=str, nargs='+', help='move folders to `temp_files_path`')
    parser.add_argument('--clear_cache', '-cc', action='store_true', help='clear all files in `temp_files_path`')
    parser.add_argument('--obfuscate_tested_codes', '-oc', action='store_true', help='obfuscate all tested codes')
    parser.add_argument('--group_by_review', '-r', action='store_true', help='go through the files and group them by reviewer')
    args = parser.parse_args()

    print("Parsed arguments:", args)

    fm = FileManager(args.cfg)
    if args.clear_cache:
        print("Clearing cache")
        fm.clear_cache()
    if args.move_files:
        if args.group_by_review:
            print("Moving files:", args.move_files, "and grouping by reviewer")
            fm.get_all_by_review([True] * len(args.move_files), *args.move_files)
        else:
            print("Moving files:", args.move_files)
            fm.get_all_by_problem([True] * len(args.move_files), *args.move_files)
    if args.move_directories:
        if args.group_by_review:
            print("Moving directories and grouping by reviewer:", args.move_directories)
            fm.get_all_by_review([False] * len(args.move_directories), *args.move_directories)
        else:
            print("Moving directories:", args.move_directories)
            fm.get_all_by_problem([False] * len(args.move_directories), *args.move_directories)
    if args.obfuscate_tested_codes:
        print("Obfuscating tested codes")
        fm.obfuscate_tested_codes()