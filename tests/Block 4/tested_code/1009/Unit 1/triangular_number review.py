




n = int(input("Enter a positive integer n: "))


triangle_sum = 0
i = 1


if n <= 0:
    print("Please enter a positive integer.")
else:
    
    while i <= n:
        triangle_sum += i
        i += 1

    
    print(f"The {n}th triangle number is {triangle_sum}.")
