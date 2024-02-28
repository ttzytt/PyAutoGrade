



user_input = int(input('Type in a number: '))
user_input_factorial = 1
countdown = 1


while countdown <= user_input:
    user_input_factorial = user_input_factorial * countdown
    countdown = countdown +1


print('The value of n! equals to ' + str(user_input_factorial) +'.')
