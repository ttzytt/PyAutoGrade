



import random


a = input("Enter 'rock', 'paper', or 'scissors': ").lower()


b = random.choice(['rock', 'paper', 'scissors'])


print("I choose " + b + '.')


if a == b:
    print("We tie.")  

elif (a == 'rock' and b == 'paper') or (a == 'paper' and b == 'scissors') or (a == 'scissors' and b == 'rock'):
    print("You win")  

else:
    print('I win')  
