

import random

random.seed()



user = input("Enter 'rock', 'paper', or 'scissors': ")
computer = random.choice(['rock', 'paper', 'scissors'])

print("I choose", computer)

if (user == computer):
    print('We tie.')


elif (user == 'paper' and computer == 'rock') or (user == 'scissors' and
      computer == 'paper') or (user == 'rock' and computer == 'scissors'):
    print('You won.') 

else:
    print('I win.')
