



user_input = int(input('Enter an integer: '))
print()

def factorial(user_input):
    
    count = 0
    result_of_factorial = 1
    while count < user_input:
        count = count + 1
        result_of_factorial = result_of_factorial * count
    return result_of_factorial
 
print(str(user_input) + '! is ' + str(factorial(user_input)))
print()


def triangular_number(n):
    
    count = 0
    triangular_number = 0
    while count < user_input:
        count = count + 1
        triangular_number = triangular_number + count
    return triangular_number

print('Triangular number: ' + str(triangular_number(user_input)))
print()

def new_triangular_number(n):
    
        count = n
        new_triangular_number = 0
        while count > 0:
            new_triangular_number = new_triangular_number + count
            count = count - 2
        return new_triangular_number

print('''The "new" triangular number: ''' + str(new_triangular_number(user_input)))


