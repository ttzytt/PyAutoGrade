



import random

human_input = input('Enter rock, scissor or paper: ') 
random.seed()
computer_input = random.choice(['rock','paper', 'scissor'])
print(computer_input)

if computer_input == 'rock':
    if human_input == 'paper':
        print('You win!')
    elif human_input == 'scissor':
        print('I win!')
if computer_input == 'paper':
    if human_input == 'rock':
        print('I win!')
    elif human_input == 'scissor':
        print('You win!')
if computer_input == 'scissor':
    if human_input == 'rock':
        print('I win!')
    elif human_input == 'paper':
        print('You win!')
    
if computer_input == human_input:
    print('We tie!')

