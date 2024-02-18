



n = int(input("Choose an positive integer: ")) 
i = 1 
factorial = 1
while i <= n:
    factorial = factorial * i
    i = i + 1
print(f"The factorial of {n} is {factorial}")


i = 1
triangular = 0
while i <= n:
    triangular = triangular + i
    i = i + 1

print(f"The traingular number of {n} is {triangular}.") 


if (n % 2) == 0:
    i = 0
    new_triangular = 0
    while i <= n:
        new_triangular = new_triangular + i
        i = i + 2
else:
    i = 1
    new_triangular = 0
    while i <= n:
        new_triangular = new_triangular + i
        i = i + 2


print(f"The new traingular number of {n} is {new_triangular}.") 



