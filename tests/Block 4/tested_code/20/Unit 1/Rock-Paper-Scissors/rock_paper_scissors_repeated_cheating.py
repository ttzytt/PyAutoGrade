
import random

choices = ["rock", "paper", "scissors"]


user_choice = input("Choose Rock, Paper, Scissors, or 'quit' to exit: ")


while not (user_choice == 'quit'):
    
    while not (user_choice == 'quit'):
        print("Please choose Rock, Paper, Scissors, or 'quit' to exit.")
        user_choice = input("Choose Rock, Paper, Scissors: ")

    
    def get_computer_choice():
        if random.random() < 0.1:  
            if user_choice == "rock":
                return "paper"
            elif user_choice == "scissors":
                return "rock"
            elif user_choice == "paper":
                return "scissors"
        else:
            return random.choice(choices)

    computer_choice = get_computer_choice()

    
    print(f"You chose {user_choice}.")
    print(f"The computer chose {computer_choice}.")

    if user_choice == computer_choice:
        print("It's a tie!")
    elif (
        (user_choice == "rock" and computer_choice == "scissors")
        or (user_choice == "paper" and computer_choice == "rock")
        or (user_choice == "scissors" and computer_choice == "paper")
    ):
        print("You win!")
    else:
        print("Computer wins!")

    
    user_choice = input("Choose Rock, Paper, Scissors, or 'quit' to exit: ")

print("Thanks for playing! Goodbye.")
