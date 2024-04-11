


import random 

random.seed()

user = input("Enter 'rock' or 'paper' or 'scissors': ") 

cheat = random.choice([1,2,3,4,5,6,7,8,9,10])

if cheat == 1:   
    
    if user == 'rock': 
        comp = 'paper'

    elif user == 'paper':
        comp = 'scissors'
        
    else:
        comp = 'rock'

    print('I choose '+comp+'.')
    print('I win.')

else:
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
        

    else:
        if comp == 'rock':
            print('You win.')
        elif comp == 'scissors':
            print('We tie.')
        else:
            print('I win')
        


    
