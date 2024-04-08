












def rps_score_round(choice_1, choice_2):
    if choice_1 == choice_2:
        return 0
    elif (
        (choice_1 == 'rock' and choice_2 == 'scissors') or
        (choice_1 == 'paper' and choice_2 == 'rock') or
        (choice_1 == 'scissors' and choice_2 == 'paper')
    ):
        return 1  
    else:
        return -1  


def get_user_choice():
    while True:
        user_input = input("Enter 'rock', 'paper', or 'scissors', or 'q' to quit: ").lower()
        if user_input in ['rock', 'paper', 'scissors', 'q']:
            return user_input
        else:
            print("Invalid input. Please try again.")


total_score = 0



while True:
    
    user_choice = get_user_choice()

    
    if user_choice == 'q':
        break

    
    computer_choice = 'rock'

    
    round_result = rps_score_round(user_choice, computer_choice)

    
    print(f"You chose {user_choice}, computer chose {computer_choice}.")

    
    if round_result == 1:
        print("You win this round!")
        total_score += 1
    elif round_result == -1:
        print("You lose this round.")
        total_score -= 1
    else:
        print("It's a tie!")

    
    print(f"Your current score is {total_score}.\n")


print("Thanks for playing!")
