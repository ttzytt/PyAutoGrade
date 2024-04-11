



def factorial(n, count):
    while(count > 0):
        n = n * count
        count -= 1
        
    return n


def triangular_number(n, count):
    while(count > 0):
        n = n + count
        count -= 1
        
    return n


def new_triangular_number(n, count):
    if(n % 2 == 0): 
        count -= 2
        
    while(count > 0):
        n = n + count + 1 
        count -= 2

    return n



n = int(input('Enter an integer: ')) 
num = n 
count = num - 1

print(str(num) + '! is ' + str(factorial(n, count)))
print('Triangular number: ' + str(triangular_number(n, count)))
print('"New" triangular number: ' + str(new_triangular_number(n, count)))

