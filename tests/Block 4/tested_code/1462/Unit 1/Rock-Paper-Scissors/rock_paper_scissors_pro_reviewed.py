




import random 
random.seed()


def rps_score_round(choice_1, choice_2):

    
    if choice_1 == 'rock':
        if choice_2 == 'rock':
            return 0
        elif choice_2 == 'paper':
            return 1
        else:
            
            return -1

    elif choice_1 == 'paper':
        if choice_2 == 'rock':
            return -1
        elif choice_2 == 'paper':
            return 0
        else:
            
            return  1
        
    elif choice_1 == 'scissors':
        if choice_2 == 'rock':
            return 1
        elif choice_2 == 'paper':
            return -1
        else:
            
            return 0
    

continue_play = 'continue'
total_score = 0
print('Your score is 0 now.')

while continue_play == 'continue':

    
    choice_1 = input("Enter 'rock' or 'paper' or 'scissors': ")
    while choice_1 != 'rock' and choice_1 != 'paper' and choice_1 != 'scissors':
        print('Invalid input, try again.') 
        choice_1 = input("Enter 'rock' or 'paper' or 'scissors': ")
        
    
    choice_2 = random.choice(['rock', 'paper', 'scissors'])

    
    round_score = rps_score_round(choice_1, choice_2)
    total_score = total_score + round_score
    print('Your score is ' + str(total_score) + ' now.')

    
    continue_play = input("Enter 'continue' if you want to keep playing: ")
    print() 

print('Bye!')


