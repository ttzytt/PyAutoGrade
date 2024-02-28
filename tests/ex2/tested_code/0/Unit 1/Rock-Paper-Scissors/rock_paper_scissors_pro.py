



import random

random.seed()


def rps_score_round():
    score = 0
    if computer == player:
        score = score + 0
    elif player == 'rock' and computer == 'paper':
        score = score - 1
    elif player == 'paper' and computer == 'rock':
        score = score + 1
    elif computer == 'scissors' and player == 'paper':
        score = score - 1
    elif player == 'scissors' and computer == 'paper':
        score = score + 1
    elif computer == 'rock' and player == 'scissors':
        score = score - 1
    elif player == 'rock' and computer == 'scissors':
        score = score + 1
    return(score)

rps = 0
print('Welcome to rock paper scissors! ')
loopvar = 0
while loopvar == 0:
    player = input("Enter 'rock', 'paper', 'scissors', or 'q' to quit: ") 
    computer = random.choice(['rock', 'paper', 'scissors'])
    if player == 'q': 
        loopvar = 1
        print('Goodbye.')
    
    elif loopvar == 0:
        print('I choose ' + computer)
    elif computer == player:
        
        print('We tie.')
    elif player == 'rock' and computer == 'paper':
        print('I win.')
    elif player == 'paper' and computer == 'rock':
        print('You win.')
    elif computer == 'scissors' and player == 'paper':
        print('I win')
    elif player == 'scissors' and computer == 'paper':
        print('You win')
    elif computer == 'rock' and player == 'scissors':
        print('I win')
    elif player == 'rock' and computer == 'scissors':
        print('You win')
    else:
        print('What do you mean? Are you trying to cheat??')
    if player != 'q':
        rps = rps + rps_score_round()
        print('Your score is ' + str(rps))
    else:
        print('Your final score is ' + str(rps))
        




