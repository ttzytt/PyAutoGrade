





import random

random.seed()

player = input("Enter 'rock' or 'paper': ")

computer = random.choice(('rock','paper'))

print("I choose " + computer + ".")




if player == 'rock':
    
    if computer == 'rock':
        print('We tie.')
    elif computer == 'paper':
        print('You win.')



elif player == 'paper':
    
    if computer == 'rock':
        print('I win.')
    if computer == 'paper':
        print('We tie.')
    
