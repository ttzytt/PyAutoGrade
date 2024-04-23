


'''
This code will let the computer and the user play an infinite amount of
rock paper scissors games, as long as the user wants to.
The user can quit at any time.
'''

import random

random.seed()

response = 'again'

while response == 'again' or response == 'Again':

    computer_move = random.choice(['Rock', 'Paper', 'Scissors'])
                                                                

    user_move = input('What is your move, Rock, Paper, or Scissors? ')
    print()                                                           
    
    if computer_move == 'Rock':
        print('I choose Rock.')
        print()
        if (user_move == 'Paper') or (user_move == 'paper'):
            print('You win.')
        elif (user_move == 'Rock') or (user_move == 'rock'):
            print('We tie.')
        elif (user_move == 'Scissors') or (user_move == 'scissors'):
            print('I win.')

    elif computer_move == 'Paper':
        print('I choose Paper')
        print()
        if (user_move == 'Rock') or (user_move == 'rock'):
            print('I win.')
        elif (user_move == 'Paper') or (user_move == 'paper'):
            print('We tie.')
        elif (user_move == 'Scissors') or (user_move == 'scissors'):
            print('You win.')

    elif computer_move == 'Scissors':
        print('I choose Scissors')
        print()
        if (user_move == 'Rock') or (user_move == 'rock'):
            print('You win.')
        elif (user_move == 'Paper') or (user_move == 'paper'):
            print('I win.')
        elif (user_move == 'Scissors') or (user_move == 'scissors'):
            print('We tie.')
    print()       
    
    response = input('''Do you want to play again?  Type 'again' to play or 'quit'
to quit. ''')
    print()



print('Sorry to see you go:(')
print()
print('You will be remembered fondly') 
