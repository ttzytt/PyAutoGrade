
def factorial(n):
    
    if n == 0:
        return 1
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result

def triangular_number(n):
    
    total = 0
    for i in range(1, n + 1):
        total += i
    return total

def new_triangular_number(n):
    
    
    total = 0
    if n % 2 == 0:
        for i in range(2, n + 1, 2):
            total += i
    else:
        for i in range(1, n + 1, 2):
            total += i
    return total


num = int(input("Enter an integer: "))
print(str(num) + "! is " + str(factorial(num)))
print("Triangular number: " + str(triangular_number(num)))
print("\"New\" triangular number: " + str(new_triangular_number(num)))
