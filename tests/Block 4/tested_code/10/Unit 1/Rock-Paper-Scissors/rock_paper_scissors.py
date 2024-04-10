




import random


player_choice = input("Enter 'rock', 'paper' or 'scissors': ")
computer_choice = random.choice(['rock', 'paper', 'scissors'])


print(f"I chose {computer_choice}.")

    
if player_choice == computer_choice:
    print('We tie.')
elif player_choice == 'rock' and computer_choice == 'paper':
    print('I win')
elif player_choice == 'paper' and computer_choice == 'rock':
    print('You win')
elif player_choice == 'scissors' and computer_choice == 'rock':
    print('I win')
elif player_choice == 'scissors' and computer_choice == 'paper':
    print('You win')
elif player_choice == 'rock' and computer_choice == 'scissors':
    print('You win')
elif player_choice == 'paper' and computer_choice == 'scissors':
    print('I win')
else:               
    print( player_choice + ' is not one of the options. Please choose rock or paper.')



