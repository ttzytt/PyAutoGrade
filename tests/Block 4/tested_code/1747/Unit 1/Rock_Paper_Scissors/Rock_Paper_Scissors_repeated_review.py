


import random

random.seed() 

user = input("Enter 'rock', 'paper' or 'scissors': ") 

while user == 'rock' or user == 'paper' or user == 'scissors':

    computer = random.choice(['rock', 'paper', 'scissors']) 

    print('I choose ' + computer + '.') 

    if user == computer: 
        print('We tie.')

    
    elif user == 'rock':
        if computer == 'paper':
            print('I win.')
        elif computer == 'scissors':
            print('You win.')

    elif user == 'paper':
        if computer == 'rock':
            print('You win.')
        elif computer == 'scissors':
            print('I win.')

    elif user == 'scissors':
        if computer == 'rock':
            print('I win.')
        elif computer == 'paper':
            print('You win.')

    print()
    user = input("Enter 'rock', 'paper' or 'scissors', or 'quit' to stop playing: ") 

if user == 'quit': 
    print('I had fun. Ciao!') 


    
