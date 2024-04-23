import random 

random.seed()

human_choice = input("Enter 'rock' or 'paper'or 'scissor': ") 
computer_choice = random.choice(['rock', 'paper', 'scissor'])
random = random.randint(1, 10)
cheating = 0
if random == 1: 
    cheating = 1 

if cheating == 1:
    
    if human_choice == 'rock':
        computer_choice = 'paper'
        
    elif human_choice == 'paper':
        computer_choice = 'scissor'
        
    elif human_choice == 'scissor':
        computer_choice = 'rock'
        
    if human_choice == 'rock' or human_choice == 'paper' or human_choice == 'scissor': 
        print('I choose ' + computer_choice + '.')
        print('I win.')
        
    else:
        
        print('I choose ' + computer_choice + '.')
        print('You cannot choose anything else than rock, paper or scissor!')
        
        
else:
    print('I choose ' + computer_choice + '.')
    
    if human_choice == computer_choice:
        print('We tie.') 
    
    elif human_choice == 'rock' and computer_choice == 'scissor':
        print('You win.')
    
    elif human_choice == 'paper' and computer_choice == 'rock':
        print('You win.')
    
    elif human_choice == 'scissor' and computer_choice == 'paper':
        print('You win.') 
    
    elif human_choice == 'rock' or human_choice == 'paper' or human_choice == 'scissor':
        print('I win.') 
        
    else:
        
        print('You cannot choose anything else than rock, paper or scissor!')
        


