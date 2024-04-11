


import random

random.seed()

computer = random.randint(1,10) 
player = int(input('Pick an integer between 1 and 10: '))
    

while player != computer:

    if computer < player <= 10: 
        print('Your guess was too high, try again.')

    elif 1 <= player < computer: 
        print('Your guess was too low, try again.')

    else: 
        print('READ THE INSTRUCTIONS!')

    print() 
    player = int(input('Pick an integer between 1 and 10: '))
        

if player == computer: 
    print('You guessed the correct number!')

    
