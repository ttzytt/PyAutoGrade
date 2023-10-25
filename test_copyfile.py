import os
import sys
from pprint import pprint
sys.path.append("./src/")
from batch_test_manager import *
from file_manager import * 

fm = FileManager()
fm.get_all_by_problem("addition")