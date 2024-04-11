



import random

random.seed()

user = input("Enter 'rock', 'paper', or 'scissors': ")
comp = random.choice(['rock', 'paper', 'scissors'])

print("I choose", comp)

if (user == comp):
    print('We tie.')

elif (user == 'paper' and comp == 'rock')or (user == 'scissors' and comp == 'paper') or (user == 'rock' and comp == 'scissors'):
    print('You won.') 

else:
    print('I win.')
