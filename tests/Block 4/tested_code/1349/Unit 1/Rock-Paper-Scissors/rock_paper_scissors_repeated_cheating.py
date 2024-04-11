import random 

random.seed()

whether_quit = 0 

while whether_quit == 0:
    human_choice = input("Enter 'rock' or 'paper'or 'scissors': ") 
    computer_choice = random.choice(['rock', 'paper', 'scissors']) 
    
    random1 = random.randint(1, 10)
    cheating = 0

    
    if random1 == 1: 
        cheating = 1 
    
    if human_choice == 'quit':
        whether_quit = 1
    else:
        if cheating == 1:
            
            if human_choice == 'rock':
                computer_choice = 'paper'
        
            elif human_choice == 'paper':
                computer_choice = 'scissors'
        
            elif human_choice == 'scissors':
                computer_choice = 'rock'
        
            if human_choice == 'rock' or human_choice == 'paper' or human_choice == 'scissors': 
                print('I choose ' + computer_choice + '.')
                print('I win.')
        
            else:
                
                print('I choose ' + computer_choice + '.')
                print('You cannot choose anything else than rock, paper or scissors!')
                
        
        else:
            print('I choose ' + computer_choice + '.')
    
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
        
            else:
                
                print('You cannot choose anything else than rock, paper or scissors!')
                

print('End of the program.')
