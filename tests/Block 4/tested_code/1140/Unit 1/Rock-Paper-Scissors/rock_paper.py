


import random


player_input = input('Enter rock or paper: ')
random.seed()


bot_choice = random.choice(['rock', 'paper'])
print('I chose ' + bot_choice)


if player_input == 'rock' and bot_choice == 'rock':
    print('We tied!')
elif player_input == 'rock' and bot_choice == 'paper':
    print('I won!')
elif player_input == 'paper' and bot_choice == 'paper':
    print('We tied!')
elif player_input == 'paper' and bot_choice == 'rock':
    print('You won!')
    

else:
    print('Invalid choice; type rock or paper!')
