

'''
This code will let the computer and the user play a random game of rock paper scissors.
'''
import random

random.seed()


computer_move = random.choice(['rock', 'paper', 'scissors'])
                                                            

user_move = input('What is your move, Rock, Paper, or Scissors? ')
print()                                                          
user_move = user_move.lower()
                             
                             

print('I choose ' + computer_move + '.')
print()
    
if computer_move == user_move:
    print('We tie.')

elif computer_move == 'rock':
    print('I choose Rock.')
    print()
    if user_move == 'paper':
        print('You win.')
    elif user_move == 'scissors':
        print('I win.')

elif computer_move == 'paper':
    if user_move == 'rock':
        print('I win.')
    elif user_move == 'scissors':
        print('You win.')

elif computer_move == 'Scissors':
    if user_move == 'rock':
        print('You win.')
    elif user_move == 'paper':
        print('I win.')


