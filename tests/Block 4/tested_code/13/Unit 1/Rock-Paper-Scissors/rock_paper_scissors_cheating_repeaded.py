import random  

def get_user_choice():
    while True:
        user_choice = input("Enter 'rock', 'paper', 'scissors', or 'quit' to end the game: ").lower()
        
        if user_choice in ('rock', 'paper', 'scissors', 'quit'):
            return user_choice  
        else:
            print("Invalid choice. Please enter 'rock', 'paper', 'scissors', or 'quit'.")
            

def get_computer_choice():
    choices = ['rock', 'paper', 'scissors']
    cheating = random.random() < 0.10  
    if cheating:
        return random.choice(choices)  
    else:
        return random.choice(choices)  

def determine_winner(user_choice, computer_choice):
    if user_choice == computer_choice:
        return "It's a tie!"  
    elif (
        (user_choice == 'rock' and computer_choice == 'scissors') or
        (user_choice == 'scissors' and computer_choice == 'paper') or
        (user_choice == 'paper' and computer_choice == 'rock')
    ):
        return "You win!"  
    else:
        return "Computer wins!"  

def main():
    print("Let's play Rock, Paper, Scissors!")
    while True:
        user_choice = get_user_choice()  
        if user_choice == 'quit':
            break  
        computer_choice = get_computer_choice()  
        print(f"You chose {user_choice}. Computer chose {computer_choice}.")
        
        result = determine_winner(user_choice, computer_choice)  
        print(result)  

if __name__ == "__main__":
    main()  
