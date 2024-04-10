




def factorial(n):
    n_left = n - 1
    while n_left > 0:
        n = n * n_left
        n_left -=1
    
    return n



def triangular_number(n):
    n_left = n - 1
    while n_left > 0:
        n = n + n_left
        n_left -= 1
    return n




def new_triangular_number(n):
    n_left = n - 2
    if n % 2 == 0:
        while n_left > 0:
            n = n + n_left
            n_left -= 2
    else:
        while n_left > 0:
            n = n + n_left
            n_left -= 2
    return n


n = int(input('Enter an integer: '))

print(str(n) + '! is ' + str(factorial(n)))
print('Triangular number: ' + str(triangular_number(n)))
print("'New' triangular number: " + str(new_triangular_number(n)))
