






import random 

random.seed()

user_quit = "continue"

while user_quit == "continue":
    
    user = input("Enter 'rock' or 'paper' or 'scissors': ") 

    comp = random.choice(['rock', 'paper','scissors']) 
    
    
    print('I choose '+comp+'.') 

    if user == 'rock':

        if comp == 'rock':
            print('We tie.')
        elif comp == 'paper':
            print('I win.')
        else:
            print('You win') 

    elif user == 'paper':
    
        if comp == 'rock':
            print('You win.')
        elif comp == 'paper':
            print('We tie.')
        else:
            print('I win')
        

    elif user == 'scissors':
        if comp == 'rock':
            print('You win.')
        elif comp == 'scissors':
            print('We tie.')
        else:
            print('I win')

    user_quit = input("Do you want to keep playing? Enter 'continue' or 'quit': ")

    print()


        
