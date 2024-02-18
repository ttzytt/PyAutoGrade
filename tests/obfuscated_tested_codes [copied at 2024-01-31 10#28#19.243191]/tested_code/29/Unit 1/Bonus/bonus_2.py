




n = int(input("Enter a number: "))
def new_triangular_number(n):
    if n% 2 == 0:
        new_triangular = (n/2)*((2 + n)/2)
    else:
        new_triangular = round(n/2)*((2 + n)/2)
    return(new_triangular)

print("The new triangular number is: " + str(new_triangular_number(n)))
