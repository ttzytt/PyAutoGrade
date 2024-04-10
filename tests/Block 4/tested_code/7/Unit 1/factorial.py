


user_input = int(input('Choose a number '))
counter = 1
factorial = 1
flag = False
while flag == False:
    factorial = factorial * counter
    
    if counter == user_input:
        flag = True
    counter = counter + 1   

print('Your n! number is ' + str(factorial))
