


number = int(input("Please enter a number.")) 
factnumber = number

factorial = factnumber 
while number > 1:
    factorial = factorial * (number - 1) 
    number = number - 1


print('The factorial of ' + str(factnumber) + ' is ' + str(factorial))





