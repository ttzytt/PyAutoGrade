


def factorial(n):
    user_integer = n
    factorial_solution = 1
    
    while user_integer >= 1:
        factorial_solution = user_integer * factorial_solution
        user_integer = user_integer - 1

    return factorial_solution

n = int(input('Enter an integer: '))
print(str(n) + '! is ' + str(factorial(n)))


print()


def triangular_number(n):
    user_integer = n
    triangular_number_solution = 1
    
    while user_integer > 1:
        triangular_number_solution = user_integer + triangular_number_solution
        user_integer = user_integer - 1

    return triangular_number_solution

n = int(input('Enter an integer: '))
print('Triangular number: ' + str(triangular_number(n)))


print()



def new_triangular_number(n):
    user_integer = n
    new_triangular_number_solution = 1
    
    while user_integer > 1:
        new_triangular_number_solution = user_integer + new_triangular_number_solution
        user_integer = user_integer - 2

    return new_triangular_number_solution

n = int(input('Enter an integer: '))
print('"New" Triangular number: ' + str(new_triangular_number(n)))









