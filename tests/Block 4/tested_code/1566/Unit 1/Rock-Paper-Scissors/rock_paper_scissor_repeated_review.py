


import random

make_your_choice = input('Enter rock, paper, scissor or quit: ')
random.seed()
computer_input = random.choice(['rock','paper', 'scissor'])
print(computer_input) 


if make_your_choice == 'rock':
    if computer_input == 'paper':
        print('I win')
    elif computer_input == 'scissor':
        print('You win.')
if make_your_choice == 'paper':
    if computer_input == 'rock':
        print('You win')
    elif computer_input == 'scissor':
        print('I win')
if make_your_choice == 'scissor':
    if computer_input == 'rock':
       print('I win')
    if computer_input == 'paper':
        print('You win') 
if computer_input == make_your_choice:
    print('We tie')
    
        

play_again = input('To play again type yes, type quit to quit: ')
while play_again == 'yes':
    make_your_choice = input('Enter rock, paper, scissor: ')
    random.seed()
    computer_input = random.choice(['rock','paper', 'scissor'])
    print(computer_input)
    if make_your_choice == 'rock':
        if computer_input == 'paper':
            print('I win') 
        elif make_your_choice == 'scissors':
            print("You win.")
    elif make_your_choice == 'paper':
        if computer_input == 'rock':
            print('You win')
        elif computer_input == 'scissors':
            print('I win')
    elif make_your_choice == 'scissors':
        if computer_input == 'rock':
            print('I win')
        elif computer_input == 'paper':
            print('You win') 
    elif computer_input == make_your_choice:
        print('We tie')

    play_again = input('Enter rock, paper, scissor: ')
print('Sad to see you go.')


