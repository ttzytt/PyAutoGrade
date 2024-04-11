

'''
This code will let the user and the computer play a random game
of rock paper scissors and infinite amount of times untl the user wants to stop.
The code is set so that the computer always wins 10% of the time.
'''

import random

random.seed()

response = 'again'

while response == 'again':
    user_move = input('What is your move, Rock, Paper, or Scissors? ')
    print()                                                          
    cheat = random.randint(1, 10)

    if cheat == 1:
        
        if user_move == 'Rock' or user_move == 'rock':
            print('I choose Paper.')
            print()
            print('I win.')

        elif user_move == 'Paper' or user_move == 'paper':
            print('I choose Scissors.')
            print()
            print('I win.')

        elif user_move == 'Scissors' or user_move == 'scissors':
            print('I choose Rock.')
            print()
            print('I win.')
    else:
        computer_move = random.choice(['Rock', 'Paper', 'Scissors'])
                                                            

   
        
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
        
        response = input('''Do you want to play again?

Type 'again' to play or 'quit' to quit. ''')
        print()
   

else:
    print('Sad to see you go. :(')
    print()
    print('You will be remembered fondly.')


