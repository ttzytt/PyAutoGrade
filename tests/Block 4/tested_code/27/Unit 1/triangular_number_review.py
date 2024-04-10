




n = int(input('Type in a number: '))
n_triangular = 0
countdown = 1

while countdown <= n:
    n_triangular = n_triangular + countdown
    countdown = countdown + 1
    
print('The value of the ' + str(n) + 'th triangular number is ' + str(n_triangular) + '.')


