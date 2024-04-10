



def factorial(n):
    factorial = 1
    while n >= 1:
        factorial = factorial * n
        n = n - 1
    return factorial


def triangular_number(n):
    triangular_number = 0
    while n >= 1:
        triangular_number = triangular_number + n
        n = n - 1
    return triangular_number


def new_triangular_number(n):
    new_triangular_number = n
    
    if n % 2 == 0:
        while new_triangular_number > 0:
            n += new_triangular_number - 2
            new_triangular_number -= 2
    
    else:
        while new_triangular_number > 0:
            n += new_triangular_number - 2
            new_triangular_number -= 2
        n = n + 1
            
    return n



def bonus_triangular_number(n):
    
    if n % 2 == 0:
        return int((n/2)*(n/2 + 1))
    elif n % 2 != 0:
        return int((n/2)*(n/2 + 1) + 1)
        


n = int(input("Enter an integer "))


print( str(n) + "! is " + str(factorial(n)) + ".")
print("Triangular number: " + str(triangular_number(n)))
print('"New" triangular number: ' + str(new_triangular_number(n)))
print("Bonus triangular number: " + str(bonus_triangular_number(n)))
