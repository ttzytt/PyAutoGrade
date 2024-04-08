import random
make_your_choice = input('Enter rock, scissor or paper : ')
random.seed()
rando = random.choice(['rock' or 'paper' or 'scissor'])
print(rando)
if rando == 'rock':
    if make_your_choice == 'paper':
        print('You win!')
    if make_your_choice == 'scissor':
        print('I win!')
if rando == 'paper':
    if make_your_choice == 'rock':
        print('I win!')
    if make_your_choice == 'scissor':
        print('You win!')
if rando == 'scissor':
    if make_your_choice == 'rock':
        print('I win!')
    if make_your_choice == 'paper':
        print('You win!')
    
if rando == make_your_choice:
    print('We tie!')

