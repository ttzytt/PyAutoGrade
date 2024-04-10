


import random 

random.seed()

player = input("Enter 'rock' or 'paper':") 
computer = random.choice(['rock', 'paper']) 
print('I choose ' + computer)
if computer == player: 
    print('We tie.')
elif player == 'rock' and computer == 'paper':
    print('I win.')
elif player == 'paper' and computer == 'rock':
    print('You win.')
else:
    print('What do you mean?')

    
                     
