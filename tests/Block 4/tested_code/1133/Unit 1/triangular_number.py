



n = int(input("Enter a number, n: "))


if n < 0:
    print("Please enter a non-negative integer.")
else:
    
    triangle_sum = 0
    i = 1
    
    
    while i <= n:
        triangle_sum += i
        i += 1
    
    
    print("The" + n + "th triangle number is " + triangle_sum + ".")
