




number = int(input('Type a number less than 1558: '))


count = 1 
factorial = 1 


while count <= number:
    factorial = factorial * count
    count = count + 1


print()
print('The factorial of '+ str(number) +' is '+ str(factorial) + '.')
