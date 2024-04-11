



import random

choices = ["rock", "paper", "scissors"]


user_choice = input("Choose Rock, Paper, Scissors, or 'quit' to exit: ")


while not (user_choice == 'quit'):
    
    while not (user_choice in choices or user_choice == 'quit'):
        print("Please choose Rock, Paper, Scissors, or 'quit' to exit.")
        user_choice = input("Choose Rock, Paper, Scissors: ")
        
    if user_choice == 'quit':
        break

    computer_choice = random.choice(choices)

    
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
