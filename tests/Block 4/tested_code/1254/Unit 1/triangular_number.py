


'''
The purpose of this program is to have the user input a number and return the triangular number of that
number to the user.
'''

n = int(input('Please enter a number: '))

count = 0

triangular_number = 0

while count < n:
    
    count = count + 1
    triangular_number = triangular_number + count 

print()   
print("The triangular number would be: " + str(triangular_number))

