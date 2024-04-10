



import random

random.seed()

score = 0


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


whether_continue = 'Yes'
score = 0

while whether_continue == 'Yes': 

    
    human_choice = input("Enter 'rock', 'paper', or 'scissors', or 'q' to quit: ")
    
    computer_choice = random.choice(['rock', 'paper', 'scissors']) 

    if human_choice != 'q':
        print('I choose ' + computer_choice + '.') 
        
    if human_choice == 'rock' or human_choice == 'paper' or human_choice == 'scissors':
        output_number = rps_score_round(human_choice, computer_choice)
        
        if output_number == 1:
            score = score + 1
            print('You win.')
        
        elif output_number == -1:
            score = score - 1
            print('I win.')
        
        elif output_number == 0:
            print('We tie.')
            
    elif human_choice == 'q':
        whether_continue = 'No'
        
    else:
        print('You cannot choose anything else than rock, paper or scissors!')
    
    print('You current point: ' + str(score))
        
    print() 

print('End of the program.')
       

