


import random

random.seed()

random_number = random.randint(1, 10)

player_guess = int(input('Guess the number: '))

while player_guess != random_number:
    
    
    if player_guess < random_number:
        player_guess = int(input('Too low! Guess again: '))

    if player_guess > random_number:
        player_guess = int(input('Too high! Guess again: '))




if player_guess == random_number:
    
    print('Well done! You guessed it right, it was ' + str(random_number) + '.')



