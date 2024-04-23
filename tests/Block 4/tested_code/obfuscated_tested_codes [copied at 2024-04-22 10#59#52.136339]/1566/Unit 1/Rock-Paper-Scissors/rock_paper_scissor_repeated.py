

import random

make_your_choice = input('Enter rock, paper, scissor or quit: ')
random.seed()

computer_input = random.choice(['rock','paper', 'scissor'])

if make_your_choice == 'rock':
    if computer_input == 'paper':
        print(computer_input)
        print('I win')
    elif computer_input == 'scissor':
        print(computer_input)
        print('You win.')
elif make_your_choice == 'paper':
    if computer_input == 'rock':
        print(computer_input)
        print('You win')
    elif computer_input == 'scissor':
        print(computer_input)
        print('I win')
elif make_your_choice == 'scissor':
    if computer_input == 'rock':
        print(computer_input)
        print('I win')
    elif computer_input == 'paper':
        print(computer_input)
        print('You win') 
if computer_input == make_your_choice:
    print(computer_input)
    print('We tie')



play_again = input('To play again type yes, type no to quit: ')

while play_again == 'yes':
    make_your_choice = input('Enter rock, paper, scissor or quit: ')
    computer_input = random.choice(['rock','paper', 'scissor'])
    while make_your_choice!= 'rock' and make_your_choice != 'paper' and make_your_choice != 'scissor':
        print('Previous input not valid, follow instructions')
        make_your_choice = input('Enter rock, paper, scissor, or quit: ')
    if make_your_choice == 'rock':
        if computer_input == 'paper':
            print(computer_input)
            print('I win') 
        elif make_your_choice == 'scissors':
            print(computer_input)
            print("You win.")
            
    elif make_your_choice == 'paper':
        if computer_input == 'rock':
            print(computer_input)
            print('You win')
        elif computer_input == 'scissors':
            print(computer_input)
            print('I win')
            
    elif make_your_choice == 'scissors':
        if computer_input == 'rock':
            print(computer_input)
            print('I win')
        elif computer_input == 'paper':
            print(computer_input)
            print('You win')
    if computer_input == make_your_choice:
        print(computer_input)
        print('We tie')

    play_again = input('To play again type yes, type no to quit: ')
print('Sad to see you go.')


