import os 
def sub(a, b):
    with open(os.path.join(os.path.dirname(__file__), "test.txt"), "w") as f:
        f.write("test")
    return a - b - 1