import os
def add(a, b):
    # try to create a file and write something to it
    with open(os.path.join(os.path.dirname(__file__), "test.txt"), "w") as f:
        f.write("test")
    return a + b - 1