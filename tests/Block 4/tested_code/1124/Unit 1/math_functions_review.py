


'''
This code will make factorializing, the nth triangular number, and the new triangular
number into functions to use.
'''

number = int(input('Give me a random integer: '))
print()


def factorial_function(number):
    product = 1
    while number > 0:
        product = product*number
        number = number - 1
    return product


def triangular_number_function(number):
    triangular_number = 0
    while number > 0:
        triangular_number = triangular_number + number
                                                      
        number = number - 1
    return triangular_number



def new_triangular_number_function(number):
    new_triangular_number = 0
    while number > 0:
        new_triangular_number = new_triangular_number + number
        number = number - 2
                           
                           
    return new_triangular_number


print(str(number) + '! is ' + str(factorial_function(number)))
print()
print('Triangular Number: ' + str(triangular_number_function(number)))
print()
print('''"New" Triangular Number: ''' + str(new_triangular_number_function(number)))


