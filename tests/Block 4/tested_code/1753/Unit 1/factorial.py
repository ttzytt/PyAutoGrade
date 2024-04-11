


user_integer = int(input('Pick any integer greater than or equal to 1: '))
print_user_integer = user_integer
    
    
factorial = 1


while user_integer >= 1:
    factorial = user_integer * factorial
    user_integer = user_integer - 1

print('The factorial of ' + str(print_user_integer) + ' is ' + str(factorial) + '.')




