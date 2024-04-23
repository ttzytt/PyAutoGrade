import numpy as np
import timeit
import random

def magnitudes(vectors):
    v = vectors * vectors
    return np.sqrt(v.sum(axis=1))

def silly_multiply(a,b):
    c = np.zeros((max(a.shape[0], b.shape[0]),max(a.shape[1], b.shape[1])))
    c[0:min(a.shape[0], b.shape[0]),0:min(a.shape[1], b.shape[1])] = \
    a[0:min(a.shape[0], b.shape[0]),0:min(a.shape[1], b.shape[1])] * b[0:min(a.shape[0], b.shape[0]),0:min(a.shape[1], b.shape[1])]
    return c

def sort_by_magnitude(vectors):
    m = magnitudes(vectors)
    m.sort()
    return m
    

print(silly_multiply(np.array([[1,2,3,4],[2,3,4,5]]),np.array([[1,2],[3,4],[5,6],[7,8]])))

integers = np.random.randint(1,10,100)
odd_integers = integers[integers % 2 == 1]
integers[integers % 2 == 1] *= 2
print(integers)
print(odd_integers)

print(sort_by_magnitude(np.array([[1,2,3,4],[2,3,4,5],[2,4,4,1]])))

square_side = random.randint(1,10)
a = np.random.randint(1,10,(square_side,square_side))

print(a)
for i in range(a.shape[0]):
    a[i,i] = 0
print(a)

def is_summetric(array):
    dimensions = len(array.shape)
    side_length = array.shape[0]
    sums = [array.sum(axis=i) for i in range(dimensions)]
    for n in range(side_length):
        for i in range(1,dimensions):
            if sums[0][n] != sums[i][n]:
                return False
    return True


print(is_summetric(np.array([[4,4],[4,3]])))
    
