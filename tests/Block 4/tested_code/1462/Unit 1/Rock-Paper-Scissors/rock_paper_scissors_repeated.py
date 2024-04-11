


import random
random.seed()


user_quit = "continue"

while user_quit == "continue":

    
    user_choice = input("Enter 'rock' or 'paper' or 'scissors': ") 

    
    comp_choice = random.choice(['rock', 'paper', 'scissors']) 
    print('I choose ' + comp_choice + '.') 

    
    if user_choice == 'rock':
        if comp_choice == 'rock':
            print('We tie.')
        elif comp_choice == 'paper':
            print('I win.')
        else:
            
            print('You win.') 

    elif user_choice == 'paper':
        if comp_choice == 'rock':
             print('You win.')
        elif comp_choice == 'paper':
            print('We tie.')
        else:
            
            print('I win.')
        

    elif user_choice == 'scissors':
        if comp_choice == 'rock':
            print('I win.')
        elif comp_choice == 'paper':
            print('You win.')
        else:
            
            print('We tie.')
            
    else:
        
        print('I already chose, you need to choose from rock, paper, and scissors too!')

    
    user_quit = input("Do you want to keep playing? Enter 'continue' or 'quit': ")
    if user_quit == 'quit':
        print('Bye!')
    elif user_quit != 'continue':
        print('You typed something other than "continue" or "quit"!'
              'I assume that you want to quit!')
              
    print() 


        
