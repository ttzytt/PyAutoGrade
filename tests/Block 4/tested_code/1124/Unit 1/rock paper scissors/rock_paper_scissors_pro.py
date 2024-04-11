


'''
This code will let the user and the computer play a random rock paper scissors game
repeatedly.  Also, the program will keep track of the score.
'''

import random

random.seed()



def rps_score_round(user_move, computer_move):
    
    if user_move == computer_move:
        return 0

    elif user_move == 'rock' and computer_move == 'paper':
        return -1

    elif user_move == 'paper' and computer_move == 'scissors':
        return -1

    elif user_move == 'scissors' and computer_move == 'rock':
        return -1

    elif user_move == 'paper' and computer_move == 'rock':
        return +1
        
    elif user_move == 'scissors' and computer_move == 'paper':
        return +1

    elif user_move == 'rock' and computer_move == 'scissors':
        return +1

score = 0

play_again = 'yes'

while play_again == 'yes':
    
    
    user_move = input('What is your move? rock, paper, or scissors?: ')
    
    
    if user_move != 'rock' and user_move != 'paper' and user_move != 'scissors':
        print('That is not a valid choice!')
        user_move = input('What is your move? rock, paper, or scissors?: ')
        
    
    computer_move = random.choice(['rock', 'paper', 'scissors'])
    
    print('I choose ' + computer_move + '.')
    
    score = score + rps_score_round(user_move, computer_move)
    
    
    print('The score is currently: ' + str(score))
    
    
    play_again = input('Do you want to play again? Print yes or no: ')
    print()
    if play_again != 'yes' and play_again != 'no':
        print('That is not an answer!')
        play_again = input('Do you want to play again? Print yes or no: ')
        print()
print('You really quit >:(')
print('I guess you want me to be lonely forever :(')
    
    

    
