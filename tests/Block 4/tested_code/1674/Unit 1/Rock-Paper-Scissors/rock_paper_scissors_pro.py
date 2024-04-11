

import random

player_score = 0
computer_score = 0

print("This is rock paper scissors but it keeps track of your score everytime you play a round. Have fun! ")
user_choice = input("Enter 'rock', 'paper', 'scissors', or 'quit' to quit: ").lower()

while user_choice != 'quit':
    if user_choice not in ('rock', 'paper', 'scissors'):
        print("Invalid input. Please try again.")
    else:
        computer_choice = random.choice(['rock', 'paper', 'scissors'])
        print()

        if user_choice == computer_choice:
            print("We tie! You don't gain or lose any points.")
        elif (user_choice == 'paper' and computer_choice == 'rock') or (user_choice == 'scissors' and
            computer_choice == 'paper') or (user_choice == 'rock' and computer_choice == 'scissors'):
            player_score += 1
            
            print("You won. Computer chose " + computer_choice + ".")
        else:
            print("The computer wins this round! Computer chose " + computer_choice + ".")
            computer_score += 1
            
    print("Player Score: " + str(player_score) + ", Computer Score: " + str(computer_score))
    user_choice = input("Enter 'rock', 'paper', 'scissors', or 'quit' to quit: ").lower()


print()
print("Final Score:")
print("Player Score: " + str(player_score) + ", Computer Score: " + str(computer_score))
print("Thank you for playing! ")
