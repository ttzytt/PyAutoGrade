



user_input = int(input('Type in a number: '))
user_input_triangular = 0
countdown = 1

while countdown <= user_input:
    user_input_triangular = user_input_triangular + countdown
    countdown = countdown + 1
    
print('The value of the ' + str(user_input) + 'th triangular number is ' + str(user_input_triangular) + '.')

