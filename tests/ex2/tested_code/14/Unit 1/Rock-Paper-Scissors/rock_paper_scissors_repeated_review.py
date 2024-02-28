




import random 

random.seed()

whether_quit = 0 

while whether_quit == 0: 
    
    
    human_choice = input("Enter 'rock' or 'paper'or 'scissor'(Type 'quit' to end the program): ") 
    computer_choice = random.choice(['rock', 'paper', 'scissor'])

    
    if human_choice != 'quit': 
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

    elif human_choice == 'quit':
        whether_quit = 1 

    else:
        print('You cannot choose anything else than rock, paper or scissor!')

print('End of the program.') 

    
    
