


'''
So what this program does is the plyaer inputs a random number, and the program is going to return the
factorial of the number to the player.
'''

n = int(input('Please enter a number: '))

count = 0

factorial = 1

while count < n:
    
    count = count + 1
    factorial = factorial * count
  
print()   
print("n! would be: " + str(factorial))


