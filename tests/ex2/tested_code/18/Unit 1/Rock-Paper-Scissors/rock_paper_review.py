


import random

random.seed()



computer = random.choice(['Rock', 'Paper'])
player = input('Choose rock or paper: ')


if computer == 'Rock':
    print('I choose rock.')
    if player == 'Rock' or player == 'rock':
        print('We tied.')
    elif player == 'Paper' or player == 'paper':
        print('You win!')
        

elif computer == 'Paper':
    print('I choose paper.')
    if player == 'Rock' or player == 'rock':
        print('You lose!')
    elif player == 'Paper' or payer == 'paper':
        print('We tied.')





