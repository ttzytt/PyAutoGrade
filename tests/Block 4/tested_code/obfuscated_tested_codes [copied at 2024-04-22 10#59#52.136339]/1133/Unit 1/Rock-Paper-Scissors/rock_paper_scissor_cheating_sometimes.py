



import random


def play_rps():
    choices = ["rock", "paper", "scissors"]
    
    
    if random.random() < 0.1:
        computer_choice = "rock"  
    else:
        computer_choice = random.choice(choices)  

    
    user_choice = input("Choose rock, paper, or scissors: ").lower()
    
    
    print(f"Computer chose: {computer_choice}")
    print(f"You chose: {user_choice}")

    
    if user_choice in choices:
        if user_choice == computer_choice:
            print("It's a tie!")
        elif (
            (user_choice == "rock" and computer_choice == "scissors") or
            (user_choice == "paper" and computer_choice == "rock") or
            (user_choice == "scissors" and computer_choice == "paper")
        ):
            print("You win!")  
        else:
            print("Computer wins!")  
    else:
        print("Please choose a valid option: rock, paper, or scissors.")


if __name__ == "__main__":
    play_rps()
