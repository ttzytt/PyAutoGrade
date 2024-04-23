



import random

random.seed()

player_selection = input("Enter 'rock' or 'paper': ")

computer_ = random.choice(('rock','paper'))


print("I choose " + computer + ".")


if player_selection == 'rock':
    
    if computer == 'rock':
        print('We tie.')
    elif computer == 'paper':
        print('I win.')



elif player_selection == 'paper':
    
    if computer == 'rock':
        print('You win.')
    if computer == 'paper':
        print('We tie.')
    
