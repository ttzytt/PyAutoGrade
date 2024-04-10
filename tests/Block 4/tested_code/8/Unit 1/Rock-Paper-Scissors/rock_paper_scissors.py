


import random 

random.seed()

player = input("Enter 'rock', 'paper', or 'scissors':") 
computer = random.choice(['rock', 'paper', 'scissors']) 
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
else:
    print('What do you mean?')


