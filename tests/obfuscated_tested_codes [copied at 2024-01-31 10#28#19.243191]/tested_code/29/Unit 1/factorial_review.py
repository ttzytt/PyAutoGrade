




number = int(input("Enter a number:"))
factorial = number


while number > 1:
    factorial = factorial*(number - 1)
    number = number - 1
print("The factorial of your number is: " + str(factorial))


