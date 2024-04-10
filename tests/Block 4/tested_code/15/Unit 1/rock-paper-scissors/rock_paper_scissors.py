

import random

random.seed() 

player = input("Enter 'rock', 'paper' or 'scissors': ")

computer = random.choice(('rock', 'paper', 'scissors'))

print ("I choose " + computer + ".")
if player == computer:
    print('We tie.')


if player == 'rock':
    if computer == 'paper':
        print('I win.')
    elif computer == 'scissors':
        print('You win.')

elif player == 'paper':
    if computer =='rock':
        print('You win.')
    elif computer == 'scissors':
        print('I win.')

elif player == 'scissors':
    if computer == 'rock':
        print ('I win.')
    elif computer == 'paper':
        print('You win.')



    
else:
    print("Silly! That's not rock paper scissors! :(") 
