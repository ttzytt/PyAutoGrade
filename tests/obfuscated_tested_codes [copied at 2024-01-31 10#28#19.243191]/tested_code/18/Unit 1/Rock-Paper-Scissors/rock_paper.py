


import random

random.seed()

computer = random.choice(['rock', 'paper'])
    
player = input('Choose rock or paper: ') 


if player.lower() == computer: 
    print('I choose ' + player.lower() + '.')
    print('We tied')

elif computer == 'rock': 
    print('I choose rock.')
    print('You win!')
    
elif computer == 'paper': 
    print('I choose paper.')
    print('You lose!')

else: 
    print('Try again.')

