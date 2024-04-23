


"""
#R the program function wrongly if anything else than rock or paper or scissor is entered
    for example, if the input is 'art'
    the output will be 'I choose rock. I win.'
    code preventing this need to be added.
"""

import random 

random.seed()

user = input("Enter 'rock' or 'paper' or 'scissors': ") 

if user == 'rock': 
    comp = 'paper'

elif user == 'paper':
    comp = 'scissors'
        
else:
    comp = 'rock'

print('I choose '+comp+'.')
print('I win.')
