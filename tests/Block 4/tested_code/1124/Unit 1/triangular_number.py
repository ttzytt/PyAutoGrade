




number = int(input('Give me an integer: '))
print()
number_print = number

triangular_number = 0


while number > 0:
                 
    triangular_number = triangular_number + number
    number = number - 1

    

if number_print == 1:
    print('The 1st triangular number is ' + str(triangular_number) + '.')
elif number_print == 2:
    print('The 2nd triangular number is ' + str(triangular_number) + '.')
elif number_print == 3:
    print('The 3rd triangular number is ' + str(triangular_number) + '.')
else:
    print('The ' + str(number_print) + 'th triangular number is '
          + str(triangular_number) + '.')

