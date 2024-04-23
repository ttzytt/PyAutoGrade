



n = int(input('Enter a poitive integer: '))
triangular_number = 0
i = n


while i > 0:
    triangular_number = triangular_number + i
    i = i - 1


print('The triangular number of ' + str(n) + ' is '
      + str(triangular_number) + '.')
