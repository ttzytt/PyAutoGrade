




def factorial(n):
    count = 1
    result = 1

    
    while count <= n:
        result = result * count
        count = count + 1
    return result


def triangular_number(n):
    count = 1
    result = 0

    
    while count <= user_input: 
        result = result + count
        count = count + 1
    return result

def new_triangular_number(n):
    count = 1
    result = 0

    if n % 2 == 1:
        
        while count <= (n + 1) / 2: 
            result = result + (2 * count) - 1
            count = count + 1
        return result

    else:
        
        while count <= n/2:
            result = result + (2 * count)
            count = count + 1
        return result


user_input = int(input('Enter an integer: '))
print(str(user_input) + '! is ' + str(factorial(user_input)))
print('Triangular number: ' + str(triangular_number(user_input)))
print('"New" triangular number: ' + str(new_triangular_number(user_input)))













