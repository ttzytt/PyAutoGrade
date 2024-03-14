# Structure of a testing pack

In PyAutoGrade, the smallest unit for conducting automatic grading/file movement/code obfusction is a testing pack, which should include the following files: 

-  configuration file of `.yaml` format that tells the location of other necessary folder, the list of students' file name, and the list of problems you wanted to test. In the following texts, this will be refered as the config file.
- A folder that stores the tested code. In the following texts, this will be refered as the code folder.
- A folder that stores the test cases. In the following texts, this will be refered as the test case folder.
- A folder that stores the result of file movement and obfuscation. In the following texts, this will be refered as the temp folder. 

An example of config file is listed below (example folder can be found [here](/tests/ex1/)):

```yaml
tested_code_path : ./tested_code
output_path : ./output
test_case_path : ./test_case
temp_files_path : ./temp_files
students_list:
- ^(PCS 9).*
problems_list: 
- addition
- ./folder/subtraction
- card_functions
```

And the corresponding folder structure is:

```
tests/ex1
├── config.yml
├── evaluation.py
├── output
├── temp_files
├── test_case
│   ├── addition.py
│   ├── addition.yml
│   ├── card_functions.py
│   └── folder
│       └── subtraction.py
└── tested_code
    ├── PCS 9 - Dangerous Behavior
    │   ├── addition.py
    │   └── folder
    │       └── subtraction.py
    ├── PCS 9 - Mr.Timeout
    │   ├── addition.py
    │   └── folder
    │       └── subtraction.py
    └── PCS 9 - Ms.Memout
        ├── addition.py
        └── folder
            └── subtraction.py
...
```

The `evaluation.py` in this example is the script to test the code and generate the result: 

```py 
import os
import sys 
from pprint import pprint
sys.path.append("./../../src/")
from batch_test_manager import *

bm = BatchTestManger(cfg_path="./config.yml")
test_ret = bm.test_all()
pprint(test_ret)
print(bm.export_csv())
```

# File/folder moving functionality

Sometimes you'd want to inspect students' code under a specific folder, but copying all students' code to a new folder is a tedious task. PyAutoGrade provides a functionality to move files/folders to a new location.

Use [test/ex1/](/tests/ex1/) as an example, you might want to move all students' file under `folder` to a new location. This functionality is provided in [`file_manager`](/src/file_manager.py) module. 

It is recommended to perform the file movement function through command line, an example is: 

```
 python ./src/file_manager.py -c ./tests/ex1/config.yml -md ./folder -mf addition.py
```
Each arugments' use is explained below:

- `-c` or `--config` : the path to the config file
- `-md` or `--move_directories` : the directory to move the files to
- `-mf` or `--move_files` : the files to move

And the meaning of this particular command is to move all students' `addition.py` and `subtraction.py` or other files under `folder` to a new location (configured in the `temp_file_path` of the config file).

Notice that all the file/folder path should be relative to `tested_code_path` (configured in the config file).

After running the command, you should get something like the following output in your temp folder: 

```
ex1/temp_files [ tree -L 1                       main * ] 12:56 AM
.
├── $folder_2024-03-14 00#55#26.107752
└── addition.py_2024-03-14 00#55#25.994356.py

2 directories, 0 files
```


If you forgot the arguments, you can always use `-h` or `--help` to see the help message: 

```
python ./src/file_manager.py --help         
usage: file_manager.py [-h] [--cfg CFG] [--move_files MOVE_FILES [MOVE_FILES ...]]
                       [--move_directories MOVE_DIRECTORIES [MOVE_DIRECTORIES ...]] [--clear_cache]
                       [--obfuscate_tested_codes]

Copy all students' file or folder into a folder in `temp_files_path`

options:
  -h, --help            show this help message and exit
  --cfg CFG, -c CFG     path to the config file
  --move_files MOVE_FILES [MOVE_FILES ...], -mf MOVE_FILES [MOVE_FILES ...]
                        move files to `temp_files_path`
  --move_directories MOVE_DIRECTORIES [MOVE_DIRECTORIES ...], -md MOVE_DIRECTORIES [MOVE_DIRECTORIES ...]
                        move folders to `temp_files_path`
  --clear_cache, -cc    clear all files in `temp_files_path`
  --obfuscate_tested_codes, -oc
                        obfuscate all tested codes
```

After checking students' code you might want to clear the temp folder, now you can use the `-cc` or `--clear_cache` argument to clear the temp folder. 

```
python ./src/file_manager.py -c ./tests/ex1/config.yml -cc
```

# Code Obfuscation functionality
TODO

# Testing functionality

## Configuring test case 
TODO