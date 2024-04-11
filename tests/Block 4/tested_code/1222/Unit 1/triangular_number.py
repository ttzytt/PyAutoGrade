




triangular_number = 1

changed_number = int(input("Which triangular number do you want me to calculate? "))
print()


original_number = changed_number 


while changed_number > 1:
    triangular_number = triangular_number + changed_number
    changed_number = changed_number - 1
    

print('The triangular number of ' + str(original_number) + ' is ' + str(triangular_number) + '.')
