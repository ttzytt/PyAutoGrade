





import random

random.seed()




def rps_score_round(choice_1, choice_2):
    if choice_1 == choice_2:
        return 0

    
    elif choice_1 == 'rock' and choice_2 == 'scissors':
        return 1
    
    elif choice_1 == 'paper' and choice_2 == 'rock':
        return 1
    
    elif choice_1 == 'scissors' and choice_2 == 'paper':
        return 1

    
    elif choice_1 == 'rock' or choice_1 == 'paper' or choice_1 == 'scissors':
        return -1

    elif choice_1 == 'q':
        return 2
    
    else:
        
        return -2


whether_continue = 'Yes'

while whether_continue == 'Yes': 

    
    human_choice = input("Enter 'rock', 'paper', or 'scissors', or 'q' to quit: ")
    
    computer_choice = random.choice(['rock', 'paper', 'scissors']) 

    if human_choice != 'q':
        print('I choose ' + computer_choice + '.') 

    output_number = rps_score_round(human_choice, computer_choice)
    
    if output_number == 1: 
        print('You win.')
        
    elif output_number == -1:
        print('I win.')
        
    elif output_number == 0:
        print('We tie.')
        
    elif output_number == 2:
        whether_continue = 'No'
        
    elif output_number == -2:
        print('You cannot choose anything else than rock, paper or scissor!')
        
    print() 

print('End of the program.')
       

