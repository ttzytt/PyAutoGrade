


import random 

random.seed()

player_guess = int(input('The computer has thought of a number from 1 to 10. Guess what it is.'))
computer_number = random.choice([1,2,3,4,5,6,7,8,9,10])

while player_guess != computer_number:

    if player_guess > computer_number:
        print('Too high!')
    elif player_guess < computer_number:
        print('Too low!')
    player_guess = int(input('Guess again!'))
else:
    print('You guessed correctly!')



