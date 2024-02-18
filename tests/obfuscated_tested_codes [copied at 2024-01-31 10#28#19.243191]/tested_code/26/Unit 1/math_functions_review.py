





def factorial(n):
    
    
    result =  1

    
    
    count = 1

    while count < n:
        count = count + 1
        
        
        
        result = result * count

    return result


def triangular_number(n):
    
    result = 0

    count = 0

    while count < n:
        count = count + 1
        
        
        
        result = result + count

    return result



def new_triangular_number(n):
    
    result = n

    
    count = n

    while count - 2 > 0: 
                         
    
        count = count - 2
        
        
        
        result = result + count

    return result   

def new_triangular_number_bonus(n):
    if n % 2 == 0: 
        
        
        
        return 2 * triangular_number(n/2)

    else: 
        
        
        
        
        

        return int(((n + 1) / 2)  ** 2)
    
        
        

    

input_integer = int(input('Enter an integer: '))

print(str(input_integer) + '! is ' + str(factorial(input_integer)))
print('Triangular number: ' + str(triangular_number(input_integer)))
print('"New" triangular number: ' + str(new_triangular_number(input_integer)))
