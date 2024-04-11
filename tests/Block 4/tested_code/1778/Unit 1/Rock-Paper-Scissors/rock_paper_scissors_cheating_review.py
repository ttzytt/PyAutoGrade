


import random

random.seed()



player= input('Enter rock, paper, scissors:')

if player == 'rock':
    print('You chose rock.')
    print('I chose paper.')
    print('You lose!')
elif player == 'paper':
    print('You chose paper.')
    print('I chose scissors.')
    print('You lose!')
elif player == 'scissors':
    print('You chose scissors.')
    print('I chose rock.')
    print('You lose!')
else:
    print('Please enter rock, paper, or scissors')


