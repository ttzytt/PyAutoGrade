ro = input('Enter, rock or paper : ')
import random
random.seed()
rando = random.choice(['rock' or 'paper'])
print(rando)
if rando == 'rock':
    if ro == 'paper':
        print('I win!')
if rando == 'paper':
    if ro == 'rock':
        print('You win!')
if rando == ro:
    print('We tie!')
