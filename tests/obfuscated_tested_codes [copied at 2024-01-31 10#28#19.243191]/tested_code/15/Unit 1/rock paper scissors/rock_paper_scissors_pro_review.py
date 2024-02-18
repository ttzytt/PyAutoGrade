


import random

random.seed()



def rps_score_round(choice_1, choice_2):
    
    if choice_1 == choice_2:
        return 0
    
    elif choice_1 == 'rock':
        if choice_2 == 'scissors':
            return 1
        elif choice_2 == 'paper':
            return -1
        
    elif choice_1 == 'paper':
        if choice_2 == 'rock':
            return 1
        elif choice_2 == 'scissors':
            return -1
        
    elif choice_1 == 'scissors':
        if choice_2 == 'paper':
            return 1
        elif choice_2 == 'rock':
            return -1



score = 0


win_count = 0
loss_count = 0
tie_count = 0


choice_1 = 'start'


while choice_1 != 'q':

    random.seed()
    
    
    choice_2 = random.choice(['rock', 'paper', 'scissors'])

    
    
    choice_1 = input("Enter 'rock', 'paper', or 'scissors', or 'q' to quit: ")

    
    while choice_1 != 'rock' and choice_1 != 'paper' and choice_1 != 'scissors' and choice_1 != 'q':
        
        print('you did not input one of the above functions')
        print('Please enter again')
        print()
        choice_1 = input("Enter 'rock', 'paper', or 'scissors', or 'q' to quit: ")

    
    
    if rps_score_round(choice_1, choice_2) == 1:
        print('You win')
        score += 1
        win_count += 1
        
    elif rps_score_round(choice_1, choice_2) == 0:
        print('We tie')
        tie_count += 1
    
    elif rps_score_round(choice_1, choice_2) == -1:
        print('You lose')
        score -= 1
        loss_count += 1

    
    print('your current score is ' + str(score))


print('Thanks for playing')
print('This are your Wins and Losses')
print()
print('You won ' + str(win_count) + ' time(s).')
print('You lost ' + str(loss_count) + ' time(s).')
print('You tied ' + str(tie_count) + ' times(s).')
print()
if loss_count == 0:
    print('Your Win/Loss ratio is ' + str(win_count) + '.')
elif loss_count > 0:
    print('Your Win/Loss ratio is ' + str(win_count/loss_count) + '.')





