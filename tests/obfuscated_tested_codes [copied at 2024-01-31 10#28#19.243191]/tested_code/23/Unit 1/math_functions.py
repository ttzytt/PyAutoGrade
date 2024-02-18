


def factorial(n):
    result = 1   
    for i in range(1, n+1):   
        result *= i   
    return result   


def triangular_number(n):

    sum = 0
    
    while i <= n:
        i = 0
        sum += i
        i += 1

    return sum
    
    

def new_triangular_number(n):
    if n % 2 == 0:   
        return sum(range(2, n+1, 2))   
    else:
        return sum(range(1, n+1, 2))   


user_input = int(input("Enter an integer: "))


print(str(user_input) + "! is " + str(factorial(user_input)))
print("Triangular number: " + str(triangular_number(user_input)))
print('"New" triangular number: ' + str(new_triangular_number(user_input)))

