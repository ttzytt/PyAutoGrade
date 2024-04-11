


"""
#R the program function wrongly if anything else than rock or paper  is entered
    for example, if the input is 'k'
    the output will be 'I choose paper. We tie.'
"""


import random 

random.seed()

user = input("Enter 'rock' or 'paper': ") 

comp = random.choice(['rock', 'paper']) 

print('I choose ' + comp + '.')

if user == 'rock':   

    if comp == 'rock':
        print('We tie.')
    else:
        print('I win.')

else:

    if comp == 'rock':
        print('You win.')
    else:
        print('We tie.')

