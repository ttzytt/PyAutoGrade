




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
while user_input <= 0:
    print('Invalid input. Please try again')
    user_input = int(input('Enter a positive integer: '))


print(f'user_input is {factorial(user_input)}')
print(f'Triangular number: {triangular_number(user_input)}')
print(f'"New" triangular number: {new_triangular_number(user_input)}')
