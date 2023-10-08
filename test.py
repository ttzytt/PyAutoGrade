import os
import sys 
sys.path.append("./src/")
from batch_test_manager import *

bm = BatchTestManger()
test_ret = bm.test_all()
print(test_ret)