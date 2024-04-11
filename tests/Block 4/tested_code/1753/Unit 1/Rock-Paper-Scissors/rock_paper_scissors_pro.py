





import random

random.seed()

player = input('Choose rock, paper, scissors, or quit (to leave the game): ')
    
computer = random.choice(['rock', 'paper', 'scissors'])
    
player_score = 0

def rps_score_round(choice_1, choice_2):
    
    if choice_1 == 'rock' and choice_2 == 'paper': 
        return -1
    
    elif choice_1 == choice_2: 
        return 0

    elif choice_1 == 'rock' and choice_2 == 'scissors': 
        return 1

    elif choice_1 == 'paper' and choice_2 == 'scissors': 
        return -1

    elif choice_1 == 'paper' and choice_2 == 'rock': 
        return 1

    elif choice_1 == 'scissors' and choice_2 == 'rock': 
        return -1

    elif choice_1 == 'scissors' and choice_2 == 'paper': 
        return 1
    

while player.lower() == 'rock' or player.lower() == 'paper' or player.lower() == 'scissors':
    computer = random.choice(['rock', 'paper', 'scissors'])
        
        
    rps_score = rps_score_round(player, computer)
    total_score = rps_score + player_score 
    
    if rps_score == -1: 
        print('I choose ' + computer)
        print('You lose')

    elif rps_score == 0: 
        print('I choose ' + computer)
        print('We tied')

    elif rps_score == 1: 
        print('I choose ' + computer)
        print('You win!')
        
    print('Your score is ' + str(total_score)) 
    player_score = rps_score + player_score
    print() 
    player = input('Choose rock, paper, scissors, or quit (to leave the game): ')


        
if player.lower() == 'quit': 
    print('Sorry to see you go. have a nice day!')


