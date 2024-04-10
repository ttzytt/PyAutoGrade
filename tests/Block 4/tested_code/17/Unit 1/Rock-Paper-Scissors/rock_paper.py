

import random

random.seed()



user = input("Enter 'rock' or 'paper': ")
computer = random.choice(['rock', 'paper'])

print("I choose", computer)


if (user == computer):
    print('We tie.')

elif (user == 'paper' and computer == 'rock'):
    print('You win.')

else:
    print('I win.')

