

import random
import time
random.seed()

print("Hello, lets play a game of rock paper scissors.")

time.sleep(1)

player = input("Choose one: Rock or Paper? (all lowercase)")

computer = random.choice(['rock', 'paper', 'scissors'])

if player == str('rock'):
    print('I choose paper. I win.')

elif player == str('scissors'):
    print('I choose rock. I win.')

elif player == str('paper'):
    print('I choose scissors. I win.')

