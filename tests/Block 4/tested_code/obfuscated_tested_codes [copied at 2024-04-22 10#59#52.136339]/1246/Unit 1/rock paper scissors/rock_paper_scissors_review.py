


import random

random.seed()

p_choice = input("Enter rock, paper, or scisscors, (all lowercase, no spaces): ")


if p_choice == 'paper':
    p_choice = 1
if p_choice == 'rock':
    p_choice = 2
if p_choice == 'scissors':
    p_choice = 3

c_choice = random.randint(1,3)



rand_m = random.randint(1,3)

rand_n = random.randint(1,3)

rand_z = random.randint(1,3)

if rand_z == 1:
    c_choice = rand_m
if rand_z == 2:
    c_choice = rand_n
if rand_z == 3:
    c_choice = c_choice



if c_choice == p_choice:
    if p_choice == 1:
        print('I choose paper')
        print('We tie')
    elif p_choice == 2:
        print('I choose rock')
        print('We tie')
    else:
        print('I choose scissors')
        print('We tie')

elif p_choice > c_choice:
    if p_choice == 2:
        print('I choose paper')
        print('You lose')
    elif p_choice == 3 and c_choice == 2:
        print('I choose rock')
        print('You lose')
    else:
        print('I choose paper')
        print('You win')

elif p_choice < c_choice:
    if p_choice == 1 and c_choice == 2:
        print('I choose rock')
        print('I lose')
    elif p_choice == 2:
        print('I choose scissors')
        print('You win')
    else:
        print('I choose scissors')
        print('You lose')


    
