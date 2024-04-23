import os
import sys 
from pprint import pprint
sys.path.append("./../../src/")
from batch_test_manager import *

bm = BatchTestManger(cfg_path="./config.yml")
test_ret = bm.test_problems('./file_reading', './file_writing')
pprint(test_ret)
print(bm.export_csv())