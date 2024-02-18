
input_number = int(input('Please input a positive integer: '))
def factorial(input_number):
    factorial = 1
    while input_number > 0:
        factorial = factorial * input_number
        input_number = input_number - 1
    return factorial


def triangular_number(input_number):
    triangular_number = 1
    number = input_number
    while number > 1:
        triangular_number = triangular_number + number
        number =  number - 1
    return triangular_number

def new_triangular_number(input_number):
    new_triangular_number = 0
    number = input_number
    while number > 0:
           new_triangular_number = new_triangular_number + number
           number =  number - 2
    return new_triangular_number

print(f' {input_number}! is {factorial(input_number)}')
print(f' Triangular number: {triangular_number(input_number)}')
print(f' "New" triangular number: {new_triangular_number(input_number)}')


    








    

