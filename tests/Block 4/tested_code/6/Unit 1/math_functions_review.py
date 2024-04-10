






n = int(input('Write a number '))

def factorial(n):
    count = 1
    result = 1
    while count <= n:
        result = result * count
        count = count + 1
    return result

def triangular_number(n):
    count = 1
    result = 0
    while count <= n:
        result = result + count
        count = count + 1
    return result

def new_triangular_number(n):
    if n % 2 == 0:
        count = 2
        result = 0
        while count <= n:
            result = result + count
            count = count + 2
        return result
    else:
        count = 1
        result = 0
        while count <= n:
            result = result + count
            count = count + 2
        return result



print(factorial(n))
print(triangular_number(n))
print(new_triangular_number(n))
