


import random

random.seed()


player_choice = input("Enter rock, paper, or scissors, (all lowercase, no spaces): ")



if player_choice == 'rock':
    print('I choose paper.')
elif player_choice == 'paper':
    print('I choose scissors.')
elif player_choice == 'scissors':
    print('I choose rock.')
else:
    print("You didn't type rock, paper, or scissors.")


print('I win.')
