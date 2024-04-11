


import random

random.seed()



player = input("Enter rock, paper, scissors:")
bot = random.choice(['rock' , 'paper' , 'scissors'])

if player == 'rock' and bot == 'paper':
    print('I chose paper.')
    print('You lose!')
elif player == 'rock' and bot == 'scissors':
    print('I chose scissors.')
    print('You win!')
elif player == 'paper' and bot == 'rock':
    print('You win!')
    print('I chose rock.')
elif player == 'paper' and bot == 'scissors':
    print('I chose scissors.')
    print('You lose!')
elif player == 'scissors' and bot == 'paper':
    print('I chose paper.')
    print('You win!')
elif player == 'scissors' and bot == 'rock':
    print('I chose rock.')
    print('You lose!')
elif player == bot:
    print('I chose ' + player + '.')
    print('You tie!')
else:
    print('Please enter rock, paper, or scissors')




