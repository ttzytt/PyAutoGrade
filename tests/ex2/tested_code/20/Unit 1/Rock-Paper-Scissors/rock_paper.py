





import random

random.seed()
human_input = input('Enter rock or paper: ')
computer_input = random.choice(['rock' or 'paper'])
print(computer_input)


if human_input == 'rock':
    if computer_input == 'paper':
        print('I win!')
if human_input == 'paper':
    if computer_input == 'rock':
        print('You win!')
if computer_input == human_input:
    print('We tie!')
