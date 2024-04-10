



factorial = 1

changed_number = int(input("Which factorial do you want me to calculate? "))


original_number = changed_number 


while changed_number >= 1:
    factorial = factorial * changed_number
    changed_number = changed_number - 1
    

print('The factorial of ' + str(original_number) + ' is ' + str(factorial) + '.')
