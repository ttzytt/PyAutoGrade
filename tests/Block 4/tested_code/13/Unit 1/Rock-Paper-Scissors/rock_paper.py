


import random

random.seed()


random_choice = random.randint(0,1)
if random_choice == 0:
    computer_choice = 'rock'
else:
    computer_choice = 'paper'


user_choice = input("Enter 'rock' or 'paper': ").lower()

print('I choose ' + computer_choice + '.')


if user_choice == 'paper':
    if computer_choice == 'rock':
        print('You win.')
    else: 
        print('We tie.')
else:
    if computer_choice == 'rock':
        print('We tie.')
    else: 
        print('I win.')
