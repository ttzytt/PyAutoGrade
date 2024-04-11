



import random 

random.seed()

whether_quit = 'No' 

while whether_quit == 'No': 
    
    
    human_choice = input("Enter 'rock' or 'paper'or 'scissors'(Type 'quit' to end the program): ") 
    computer_choice = random.choice(['rock', 'paper', 'scissors']) 

    
    if human_choice != 'quit': 
        print('I choose ' + computer_choice + '.')
        
    else:
        whether_quit = 'Yes'

    
    if human_choice == computer_choice:
        print('We tie.') 
    
    elif human_choice == 'rock' and computer_choice == 'scissors':
        print('You win.')
    
    elif human_choice == 'paper' and computer_choice == 'rock':
        print('You win.')
    
    elif human_choice == 'scissors' and computer_choice == 'paper':
        print('You win.')

    
    elif human_choice == 'rock' or human_choice == 'paper' or human_choice == 'scissors':
        print('I win.')

    elif whether_quit == 'No':
        
        print('You cannot choose anything else than rock, paper or scissors!')

    print() 

print('End of the program.') 

    
    
