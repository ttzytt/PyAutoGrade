


n = int(input("Write a positive integer: "))
if n < 0:

    print("Factorial is not defined for negative numbers.")
else:
    result = 1
    input_n = n
    
    while n > 0:
        result *= n
        n -= 1

    print(f"The factorial of {input_n} is {result}.")


