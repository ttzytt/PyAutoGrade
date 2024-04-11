


n = int(input('Enter an integer: '))

def factorial(n):
    count = 0
    result_of_factorial = 1
    while count < n:
        count = count + 1
        result_of_factorial = result_of_factorial * count
    return result_of_factorial
  
print(str(n) + '! is ' + str(factorial(n)))


def triangular_number(n):
    count = 0
    triangular_number = 0
    while count < n:
        
        count = count + 1
        triangular_number = triangular_number + count
    return triangular_number

print('Triangular number: ' + str(triangular_number(n)))


def new_triangular_number(n):
    if (n+1 % 2) != 0: 
        count = 0
        new_triangular_number = 0
        while count < n:
            count = count + 2
            new_triangular_number = new_triangular_number + count
        return new_triangular_number
    else:
        count = 0
        new_triangular_number = 1
        while count < n:
            count = count + 2
            new_triangular_number = new_triangular_number + count
        return new_triangular_number

print( + str(new_triangular_number(n)))


