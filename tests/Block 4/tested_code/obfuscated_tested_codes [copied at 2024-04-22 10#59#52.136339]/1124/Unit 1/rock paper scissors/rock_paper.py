




import random

random.seed()

computer_move = random.choice(['Rock', 'Paper'])

user_move = input('What is your move, Rock or Paper? ')
print()



if computer_move == 'Rock':
    print('I choose Rock.')
    print()
    if (user_move == 'Paper') or (user_move == 'paper'):
        print('You win.')
    elif (user_move == 'Rock') or (user_move == 'rock'):
        print('We tie.')

elif computer_move == 'Paper':
    print('I choose Paper')
    print()
    if (user_move == 'Rock') or (user_move == 'rock'):
        print('I win.')
    elif (user_move == 'Paper') or (user_move == 'paper'):
        print('We tie.')

 
