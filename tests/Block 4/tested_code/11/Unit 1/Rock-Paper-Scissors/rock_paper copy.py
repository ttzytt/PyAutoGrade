user = input ('Enter rock or paper: ')

user = int (user)

import random

random.seed()

me = random.choice(['rock', 'paper'])

print ('I choose ' + me)

if user == 'paper' and me == 'rock':
    print ('You win. ')
elif user == 'rock' and me == 'paper':
    print ('I win! ')
else:
    print ('We tie. ')
