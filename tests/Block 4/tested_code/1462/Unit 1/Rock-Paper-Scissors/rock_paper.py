



import random 
random.seed()


user_choice = input("Enter 'rock' or 'paper': ") 


comp_choice = random.choice(['rock', 'paper']) 
print('I choose ' + comp_choice + '.')


if user_choice == 'rock':   
    if comp_choice == 'rock':
        print('We tie.')
    else:
        
        print('I win.')

elif user_choice == 'paper':
    if comp_choice == 'rock':
        print('You win.')
    else:
        
        print('We tie.')

else:
    
    print('I already chose, you need to choose from rock and paper too!')




        
        

