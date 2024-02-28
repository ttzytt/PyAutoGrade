



import random
random.seed()



def rps_score_round(choice_1, choice_2):
    if choice_1 == choice_2:
        
        return 0
    elif (choice_1== 'paper' and choice_2 == 'scissors') or (choice_1== 'scissors' and choice_2 == 'rock') or (choice_1== 'rock' and choice_2 == 'paper'):
        
        return 1
    elif (choice_2== 'paper' and choice_1 == 'scissors') or (choice_2 == 'scissors' and choice_1 == 'rock') or (choice_2 == 'rock' and choice_1 == 'paper'):
        
        return -1
    else:
        return None

respond = 'a'
score = 0

computer = random.choice(['paper','scissors','rock'])
respond = input("Enter 'rock', 'paper', or 'scissors', or 'q' to quit: ")

while respond != 'q': 
    
    if rps_score_round(computer,respond) is None:
        respond = input('Try again: ')

    
    if rps_score_round(computer,respond) == 1:
         print("You win")
         score = score + rps_score_round(computer,respond)
         
    elif rps_score_round(computer,respond) == 0:
         print('We tie')
         score = score + rps_score_round(computer,respond)

    elif rps_score_round(computer,respond) == -1:
         print('I win')
         score = score + rps_score_round(computer,respond)
    print('score: '+ str(score)) 
    

    respond = input("Enter 'rock', 'paper', or 'scissors', or 'q' to quit: ")

if respond == 'q':
    print('The game ends') 
