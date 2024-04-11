



import random

random.seed()


answer = input(" Enter 'rock' or 'paper' ")




if random.randint(0,1) == 1:
    print('I choose paper')
    if answer == 'rock':
        print('I win')
    else:
        print('We tie')



else:
    print('I choose rock')
    if answer == 'rock':
        print('We tie')
    else:
        print('You win')

