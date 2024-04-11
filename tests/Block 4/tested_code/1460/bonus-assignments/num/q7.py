import numpy as np
import timeit

a_array = np.arange(0,1000)
a_list = list(a_array)
b_array = np.arange(0,1000) + 0.5
b_list = list(b_array)

def multiply_1():
    product = a_array * b_array


def multiply_2():
    product = []
    for i in range(1000):
        product.append(a_array[i] * b_array[i])


def multiply_3():
    product = [a_array[i] * b_array[i] for i in range(1000)]

print(timeit.timeit(multiply_1, number = 1000))
print(timeit.timeit(multiply_2, number = 1000))
print(timeit.timeit(multiply_3, number = 1000))
