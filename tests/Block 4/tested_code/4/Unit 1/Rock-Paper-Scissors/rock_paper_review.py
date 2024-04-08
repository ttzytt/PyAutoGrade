


import random


Answer = input(" Enter 'rock' or 'paper'")

if random.randint(0,1) == 1:
    print('I choose paper')
    if Answer == 'rock':
        print('I win')
    if Answer == 'paper':
        print('We tie')

else:
    print('I choose rock')
    if Answer == 'rock':
        print('We tie')
    if Answer == 'paper':
        print('You win')

