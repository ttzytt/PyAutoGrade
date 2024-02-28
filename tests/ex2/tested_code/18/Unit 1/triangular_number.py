


user_integer = int(input('Pick any integer greater than 1: '))
    
    
triangular_num = 1


while user_integer > 1:
    triangular_num = user_integer + triangular_num
    user_integer = user_integer - 1

print('The triangle number of ' + str(user_integer) + ' is ' + str(triangular_num) + '.')
