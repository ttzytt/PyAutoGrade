





def factorial(n):
    factorial = 1
    while n >= 1:
        factorial = factorial * n
        n = n - 1
    return factorial


n = int(input("Enter an integer "))


def triangular_number(n):
    triangular_number = 1
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








print( str(n) + "! is " + str(factorial(n)) + ".")
print("Triangular number: " + str(triangular_number(n)))
print('"New" triangular number: ' + str(new_triangular_number(n)))
