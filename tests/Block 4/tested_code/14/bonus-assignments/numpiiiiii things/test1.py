import numpy as np

x = np.array([[1, 2], [3, 4]])
y = np.array([[5, 6]])
a = np.concatenate((x, y), axis=0)
print(a)
b = np.concatenate((x, y), axis=1)
print(b)
