



import random

random.seed()

bot_choice = random.randint(1,10)


player_input = int(input('Guess an integer 1-10: '))


while player_input != bot_choice:
    if player_input > bot_choice:
        print('Your guess is too high, try again!')
    elif player_input < bot_choice:
        print('Your guess is too low, try again!')
    else:
         print('Invalid choice; enter an integer 1-10!')

    
    player_input = int(input('Enter an integer 1-10: '))

print('You got it! Great job!')


