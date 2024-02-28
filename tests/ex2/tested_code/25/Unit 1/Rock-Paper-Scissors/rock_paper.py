


import random

random.seed()



user = input('choose rock or paper: ')



me = random.choice(['rock','paper'])
print('i choose ' + me)


if user == 'rock' and me == 'paper':
    print('i win')
elif user == 'rock' and me == 'rock':
    print('we tie')
elif user == 'paper' and me == 'rock':
    print('you win')
elif me == 'paper' and user == 'paper':
    print('we tie')

