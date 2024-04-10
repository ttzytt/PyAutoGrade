


import random
random.seed()


user_choice = input("Enter 'rock' or 'paper' or 'scissors': ") 


if user_choice == 'rock':
    comp_choice = 'paper'
elif user_choice == 'paper':
    comp_choice = 'scissors'
elif user_choice == 'scissors':
    comp_choice = 'rock'
else:
    
    print('You need to choose from rock, paper, and scissors.')
    comp_choice = "nothing, but I still win because you didn't choose"

print('I choose ' + comp_choice + '.')
print('I win.')
