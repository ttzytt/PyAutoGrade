


import random
random.seed()
computer_move = random.choice(['Rock', 'Paper', 'Scissors'])
                                                            

user_move = input('What is your move, Rock, Paper, or Scissors?')
                                                                 

if computer_move == 'Rock':
    print('I choose Rock.')
    if (user_move == 'Paper') or (user_move == 'paper'):
        print('You win.')
    elif (user_move == 'Rock') or (user_move == 'rock'):
        print('We tie.')
    elif (user_move == 'Scissors') or (user_move == 'scissors'):
        print('I win.')

elif computer_move == 'Paper':
    print('I choose Paper')
    if (user_move == 'Rock') or (user_move == 'rock'):
        print('I win.')
    elif (user_move == 'Paper') or (user_move == 'paper'):
        print('We tie.')
    elif (user_move == 'Scissors') or (user_move == 'scissors'):
        print('You win.')

elif computer_move == 'Scissors':
    print('I choose Scissors')
    if (user_move == 'Rock') or (user_move == 'rock'):
        print('You win.')
    elif (user_move == 'Paper') or (user_move == 'paper'):
        print('I win.')
    elif (user_move == 'Scissors') or (user_move == 'scissors'):
        print('We tie.')


