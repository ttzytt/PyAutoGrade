


import random

random.seed()

player_score = 0
computer_score = 0

print("This is rock paper scissors, and it keeps track of your score every time you play a round. Have fun!")



def rps_score_round(choice_1, choice_2):
    if choice_1 == choice_2:
        return 0

    elif ((choice_1 == 'paper' and choice_2 == 'rock') 
            or (choice_1 == 'scissors' and choice_2 == 'paper')
            or (choice_1 == 'rock' and choice_2 == 'scissors')):
        return +1

    else:
        return -1


user_choice = input("Enter 'rock', 'paper', 'scissors', or 'quit' to quit: ").lower()

while user_choice != 'quit':
    if user_choice not in ['rock', 'paper', 'scissors']:
        print("Invalid input. Please try again.")
    else:
        
        computer_choice = random.choice(['rock', 'paper', 'scissors'])

        print("Computer chose:", computer_choice)

        result = rps_score_round(user_choice, computer_choice)

        if result == 0:
            print("It's a tie!")
        elif result == 1:
            print("You win this round!")
            player_score += 1
        else:
            print("Computer wins this round!")
            computer_score += 1

        print("Your score:", player_score)
        print("Computer's score:", computer_score)

    print()
    user_choice = input("Enter 'rock', 'paper', 'scissors', or 'quit' to quit: ").lower()


print("Thanks for playing!")
print("Your final score:", player_score)
print("Computer's final score:", computer_score)

