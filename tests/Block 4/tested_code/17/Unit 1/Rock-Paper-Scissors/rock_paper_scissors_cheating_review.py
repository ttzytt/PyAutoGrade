





human_choice = input("Enter 'rock' or 'paper'or 'scissor': ") 
computer_choice = '0'


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
    print('You cannot choose anything else than rock, paper or scissor!')

    

