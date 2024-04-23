




n = int(input("Enter a number, n: "))


fact = 1  
count = 1  
factorial_expression = "1"  


while count <= n:
    fact *= count  
    if count > 1:
        factorial_expression += f" * {count}"  
    count += 1  


print(+ n! = {factorial_expression} = {fact}")

