


 


import random
random.seed()

def rps_score_round(choice_1, choice_2):
    if choice_1 == choice_2:
        return 0
    elif (choice_1 == 'paper' and choice_2 == 'scissors') or (choice_1 == 'scissors' and choice_2 == 'rock') or (choice_1 == 'rock' and choice_2 == 'paper'):
        return -1
    elif (choice_2 == 'paper' and choice_1 == 'scissors') or (choice_2 == 'scissors' and choice_1 == 'rock') or (choice_2 == 'rock' and choice_1 == 'paper'):
        return 1
    else:
        return None
human = 'a'
score = 0
while human != 'q':
    human = input("Enter 'rock', 'paper', or 'scissors', or 'q' to quit: ")
    computer = random.choice(['paper', 'rock', 'scissors'])
    
    if rps_score_round(human,computer) is not None :
        score = score + rps_score_round(human,computer)
          
        print('I choose ' + computer + '.')
        print("Score: " + str(score))

    elif human != 'q':
        print("Try again!")

  


