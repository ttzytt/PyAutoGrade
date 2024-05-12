import sys
sys.path.append('../src/')
from stdIO_simulator import *
import multiprocessing
import time
if __name__ == "__main__":
    fake_stdio = StdIOSimulator('./test_module.py')
    # run the test module on another process
    p = multiprocessing.Process(target=fake_stdio.load_and_exec_module)
    p.start()
    fake_stdio.write_input("Hello, World!")
    print(fake_stdio.get_output() + " from main process")
    var1 = fake_stdio.get_output()
    var2 = fake_stdio.get_output()
    print(var1, var2, " from main process", int(var1) + int(var2))  
    p.join()  