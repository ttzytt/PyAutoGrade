





def factorial(n):
    n_factorial = 1
    countdown = 1

    
    while countdown <= n: 
        n_factorial = n_factorial * countdown
        countdown = countdown +1
        
    
    return n_factorial

def triangular_number(n):
    n_triangular = 0
    countdown = 1

    while countdown <= n:
        n_triangular = n_triangular + countdown
        countdown = countdown + 1
    
    return n_triangular






def new_triangular_number(n):

    
    if n % 2 == 1:
        
        return int((n + 1) * (n + 1) / 4)
    
    if n % 2 == 0:
        return int((n / 2) * (n / 2 + 1))

user_input = int(input('Enter an integer: '))



print(str(user_input) + '! is ' + str(factorial(user_input)))
print('Triangular number: ' + str(triangular_number(user_input)))
print('"New" triangular number: ' + str(new_triangular_number(user_input)))


    

    
