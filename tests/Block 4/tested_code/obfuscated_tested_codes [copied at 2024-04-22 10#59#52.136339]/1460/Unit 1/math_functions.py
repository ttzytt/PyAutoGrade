







def factorial(n):
    product = 1
    count = 1
    while count <= n:
        product = product * count
        count = count + 1


    return product

def triangular_number(n):
    sum_var = 0
    count = 1
    while count <= n:
        sum_var = sum_var + count
        count = count + 1


    return sum_var

def new_triangular_number(n):
    if n % 2: 
        
        
        return round((n+1)/2)**2
        
        
    else: 
        return 2 * triangular_number(int(n/2))

user_number = int(input('Enter an integer: '))
print(f'{user_number}! is {factorial(user_number)}')
print(f'Triangular number: {triangular_number(user_number)}')
print(f'"New" Triangular Number is {new_triangular_number(user_number)}')

