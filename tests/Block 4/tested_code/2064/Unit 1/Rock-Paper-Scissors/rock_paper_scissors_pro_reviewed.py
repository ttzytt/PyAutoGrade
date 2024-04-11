



import random

random.seed()


def rps_score_round(choice_1, choice_2): 
    if(choice_1 == choice_2): 
        bonus = 0 
    elif(((choice_1 == 'rock') and (choice_2 == 'paper')) or
        ((choice_1 == 'scissors') and (choice_2 == 'rock')) or
        ((choice_1 == 'paper') and (choice_2 == 'scissors'))):
            bonus = -1 
    else:
        bonus = 1 

    return bonus 



choice_1 = input('Enter \'rock\', \'paper\', or \'scissors\', or \'q\' to quit: ')
score = 0

while(choice_1 != 'q'): 
    choice_2 = random.choice(['rock', 'paper', 'scissors']) 
    if ((choice_1.lower() == 'rock') or
        (choice_1.lower() == 'scissors') or
        (choice_1.lower() == 'paper')): 
        score += rps_score_round(choice_1.lower(), choice_2)
        print() 
        print(str(score)) 
    else:
        print('That\'s not valid. Try agian.') # tells user to try again

    print() #adds new line
    choice_1 = input('Enter \'rock\', \'paper\', or \'scissors\', or \'q\' to quit: ')

print() #adds new line
print('See you later! :)')
    
