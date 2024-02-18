import os
import sys 
from pprint import pprint
sys.path.append("./src/")
from batch_test_manager import *

bm = BatchTestManger(cfg_path="./tests/obfuscated_tested_codes [copied at 2024-01-31 10#28#19.243191]/cfg.yml")
test_ret = bm.test_problems('./Unit 1/Cards/card_functions')
pprint(test_ret)
print(bm.export_csv())