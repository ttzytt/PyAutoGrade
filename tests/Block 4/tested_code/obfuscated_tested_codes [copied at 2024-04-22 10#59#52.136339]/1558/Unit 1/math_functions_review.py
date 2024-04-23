


"""
This program has three functions, A function factorial(n) that returns n!
(just the number, not a sentence).
A function triangular_number(n) that returns 1 + 2 +... + n.
A function new_triangular_number(n) that returns
2 + 4 + 6 + ... + n if n is even,
and returns 1 + 3 + 5 + ... + n if n is odd.
"""

def factorial(n):

    
    factorial = 1
    
    while n > 0:
        factorial = n * factorial 
        n = n - 1  
    return factorial 
    

def triangular_number(n):
     
    triangle_number = 0 
    while n > 0:  
        triangle_number = n + triangle_number 
        n = n - 1 
    return triangle_number    

def new_triangular_number(n):

    new_triangle_number = 0 
    while n > 0:  
        new_triangle_number = n + new_triangle_number 
        n = n - 2 
    return new_triangle_number
        

user_input = int(input('Enter a positive integer: '))



print(f'user_input is {factorial(user_input)}')
print(f'Triangular number: {triangular_number(user_input)}')
print(f'"New" triangular number: {new_triangular_number(user_input)}')

