

import random

player_input = int(input('Please select a number 1 - 10: '))
computer_input =  random.randrange(1,10)


if player_input > (10) or player_input < 0:
    print('Your number is not within the 1-10 range. ')
    player_input = int(input('Please select a number 1-10: '))
    

while player_input != computer_input:
    if (player_input) > (computer_input):
        print('Too high')
        player_input = int(input('Enter another number: '))
    if (player_input) < (computer_input):
        print('Too low')
        player_input = int(input('Enter another number: '))
else: 
    print('You got it!')
        
    
    
