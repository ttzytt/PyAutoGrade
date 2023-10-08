import os
import sys 
from pprint import pprint
sys.path.append("./src/")
from batch_test_manager import *

bm = BatchTestManger()
test_ret = bm.test_all()
pprint(test_ret)