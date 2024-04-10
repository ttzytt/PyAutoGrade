


import random

print("Hello, lets play a game of rock paper scissors.")

player = input("Choose one: Rock, Paper, Or Scissors? (all lowercase) ")

computer = random.choice(['rock', 'paper', 'scissors'])


if player == str('rock'):
    print('I choose paper. I win.')

elif player == str('scissors'):
    print('I choose rock. I win.')

elif player == str('paper'):
    print('I choose scissors. I win.')

