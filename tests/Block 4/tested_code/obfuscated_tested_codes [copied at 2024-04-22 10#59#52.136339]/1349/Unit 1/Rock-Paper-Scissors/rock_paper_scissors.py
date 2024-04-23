





import random 

random.seed()

human_choice = input("Enter 'rock' or 'paper'or 'scissors': ") 
computer_choice = random.choice(['rock', 'paper', 'scissors']) 
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
