


import random

random.seed()


user = input("enter rock, paper, scissors or enter 'quit' to quit: ")


me = random.choice(['rock','paper','scissors'])
print('i choose ' + me)

while user != 'quit':
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
if user == 'quit':
    print ('okay, bye bye')


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
