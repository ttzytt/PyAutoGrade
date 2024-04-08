


import random

random.seed()


player_choice = input("Enter rock, paper, or scisscors (all lowercase): ")


if player_choice == 'paper':
    player_choice = 1
if player_choice == 'rock':
    player_choice = 2
if player_choice == 'scissors':
    player_choice = 3


computer_choice = random.randint(1,3)


if computer_choice == player_choice:
    
    if player_choice == 1:
        print('I choose paper')
        print('We tie')
        
    elif player_choice == 2:
        print('I choose rock')
        print('We tie')
        
    else:
        print('I choose scissors')
        print('We tie')


elif player_choice > computer_choice:
    
    if player_choice == 2:
        print('I choose paper')
        print('You lose')
        
    elif player_choice == 3 and computer_choice == 2:
        print('I choose rock')
        print('You lose')
        
    else:
        print('I choose paper')
        print('You win')


elif player_choice < computer_choice:
    
    if player_choice == 1 and computer_choice == 2:
        print('I choose rock')
        print('I lose')
        
    elif player_choice == 2:
        print('I choose scissors')
        print('You win')
        
    else:
        print('I choose scissors')
        print('You lose')
        
    
