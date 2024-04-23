

"""
#R the program function wrongly if anything else than rock or paper or scissor is entered
    for example, if the input is 'art'
    the output will be 'I choose rock. You win.'
"""

import random 

random.seed()

user = input("Enter 'rock' or 'paper' or 'scissors': ") 

comp = random.choice(['rock', 'paper','scissors']) 

print('I choose '+comp+'.')


if user == 'rock':

    if comp == 'rock':
        print('We tie.')
    elif comp == 'paper':
        print('I win.')
    else:
        print('You win') 

elif user == 'paper':
    
    if comp == 'rock':
        print('You win.')
    elif comp == 'paper':
        print('We tie.')
    else:
        print('I win')
        

else:
    if comp == 'rock':
        print('You win.')
    elif comp == 'scissors':
        print('We tie.')
    else:
        print('I win')
        
        
