


import random



Answer = input("Enter 'rock' or 'paper' or 'scissors' ")

if random.randint(0,2) == 0:
    print('I choose rock')
    if Answer == 'rock':
        print('We tie')
    if Answer == 'paper':
        print('You win')
    if Answer == 'scissors':
        print('I win')



elif random.randint(0,2) == 1:
    print('I choose paper')
    if Answer == 'rock':
        print('I win')
    if Answer == 'paper':
        print('We tie')
    if Answer == 'scissors':
        print('You win')

else:
    print('I choose scissors')
    if Answer == 'rock':
        print('You win')
    if Answer == 'paper':
        print('I win')
    if Answer == 'scissors':
        print('We tie')
