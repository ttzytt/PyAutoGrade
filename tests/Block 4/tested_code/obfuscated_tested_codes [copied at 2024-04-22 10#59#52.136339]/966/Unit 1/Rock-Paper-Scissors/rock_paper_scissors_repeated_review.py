


import random

random.seed()

"""
# defines user
user = input("enter rock, paper, scissors or enter 'quit' to quit: ")

# defines me
me = random.choice(['rock','paper','scissors'])
print('i choose ' + me)
"""

user = input("enter rock, paper, scissors or enter 'quit' to quit: ")



while user != 'quit':


    me = random.choice(['rock','paper','scissors'])
    print('i choose ' + me)


    if user == 'rock':
        if me == 'paper':
            print('i win')
        elif me == 'rock':
            print('we tie')
        elif me == 'scissors':
            print('you win')

    if user == 'paper':
        if me == 'rock':
            print('you win')
        elif me == 'paper':
            print('we tie')
        elif me == 'scissors':
            print('i win')

    if user == 'scissors':
        if me == 'scissors':
            print('we tie')
        elif me == 'paper':
            print('i win')
        elif me == 'rock':
            print('you win')


    user = input("enter rock, paper, scissors or enter 'quit' to quit: ")
    
"""
if user == 'rock':
    if me == 'paper':
        print('i win')
    elif me == 'rock':
        print('we tie')
    elif me == 'scissors':
        print('you win')

if user == 'paper':
    if me == 'rock':
        print('you win')
    elif me == 'paper':
        print('we tie')
    elif me == 'scissors':
        print('i win')

if user == 'scissors':
    if me == 'scissors':
        print('we tie')
    elif me == 'paper':
        print('i win')
    elif me == 'rock':
        print('you win')
"""


