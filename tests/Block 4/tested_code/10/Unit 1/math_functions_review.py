



def factorial(user_number):
    factorial = user_number
    factcounter = user_number
    while factcounter > 1:
        factorial = factorial * (factcounter - 1) 
        factcounter = factcounter - 1
        
    return(factorial)

def triangle_number(user_number):
    triangle_number = user_number
    triangle_number = (triangle_number * (user_number + 1)) / 2
    return(triangle_number)

def new_triangle_number(user_number):
    new_triangle_number = 0
    if user_number %2 == 0:
        counter = 0
        while new_triangle_number <= user_number:
            new_triangle_number = new_triangle_number + counter
            counter = counter + 2

    else:
        counter = 1
        
        while new_triangle_number <= user_number:
            new_triangle_number = new_triangle_number + counter
            counter = counter + 2
            
    return(new_triangle_number)

user_number = int(input('Enter an integer: '))
print('n! = ' + str(factorial(user_number)))
print('Triangular number: ' + str(round(triangle_number(user_number))))
print('"New" triangular number:' + str(new_triangle_number(user_number)))

