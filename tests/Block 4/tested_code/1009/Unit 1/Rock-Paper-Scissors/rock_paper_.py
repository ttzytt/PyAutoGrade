

import random


play_again = True


while play_again:
    
    
    user_choice = input("Choose Rock, Paper, Scissors, or 'quit' to exit: ")

    
    if user_choice == 'quit':
        print("Thanks for playing! Goodbye.")
        play_again = False
    else:
        
        choices = ["rock", "paper"]

        
        
        computer_choice = random.choice(choices)

        
        if user_choice in choices:
            
            print(f"You chose {user_choice}.")
            print(f"The computer chose {computer_choice}.")

            
            if user_choice == computer_choice:
                print("It's a tie!")
            elif (
                (user_choice == "paper" and computer_choice == "rock")
                or (user_choice == "scissors" and computer_choice == "paper")
            ):
                print("You win!")
            else:
                print("Computer wins!")
        else:
            
            print("Invalid choice. Please choose Rock, Paper, or 'quit' to exit.")
