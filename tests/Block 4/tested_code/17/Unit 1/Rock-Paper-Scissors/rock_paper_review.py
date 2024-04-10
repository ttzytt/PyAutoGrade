



import random

random.seed()

user = input("Enter 'rock' or 'paper': ")
comp = random.choice(['rock', 'paper'])

print("I choose", comp)

if (user == comp):
    print('We tie.')

elif (user == 'paper' and comp == 'rock'):
    print('You won.')

else:
    print('I win.')

