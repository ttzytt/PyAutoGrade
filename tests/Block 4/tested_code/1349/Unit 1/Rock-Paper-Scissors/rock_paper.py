


import random 

random.seed()

human_choice = input("Enter 'rock' or 'paper': ") 
computer_choice = random.choice(['rock', 'paper'])
print('I choose ' + computer_choice + '.')
   
if human_choice == computer_choice:
    print('We tie.')
    
elif human_choice == 'rock' and computer_choice == 'paper':
    print('I win.')
    
elif human_choice == 'paper' and computer_choice == 'rock':
    print('You win.')
    
else:
    
    print('You cannot choose anything else than rock or paper!')
