


import random

random.seed()
print('Welcome to rock paper scissors! Type quit to stop playing.')
loopvar = 0
while loopvar == 0:
    player = input("Enter 'rock', 'paper', or 'scissors':") 
    
    if player == 'quit': 
        loopvar = 1
        print('Goodbye.')
    computer = random.choice(['rock', 'paper', 'scissors'])
    
    if loopvar == 0:
        print('I choose ' + computer)
    if computer == player:
        
        print('We tie.')
    elif player == 'rock' and computer == 'paper':
        print('I win.')
    elif player == 'paper' and computer == 'rock':
        print('You win.')
    elif computer == 'scissors' and player == 'paper':
        print('I win')
    elif player == 'scissors' and computer == 'paper':
        print('You win')
    elif computer == 'rock' and player == 'scissors':
        print('I win')
    elif player == 'rock' and computer == 'scissors':
        print('You win') 
    
