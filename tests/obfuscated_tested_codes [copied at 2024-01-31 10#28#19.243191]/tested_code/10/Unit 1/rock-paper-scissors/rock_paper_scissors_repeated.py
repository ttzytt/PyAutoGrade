


import random

def play_rock_paper_scissors(user_choice, computer_choice):
    
    
    if user_choice == computer_choice:
        return "It's a tie!"
    elif user_choice == "rock":
        if computer_choice == "scissors":
            return "You win!"
        else:
            return "Computer wins!"
    elif user_choice == "paper":
        if computer_choice == "rock":
            return "You win!"
        else:
            return "Computer wins!"
    elif user_choice == "scissors":
        if computer_choice == "paper":
            return "You win!"
        else:
            return "Computer wins!"

print("Welcome to Rock, Paper, Scissors!")
print("Enter your choice: 'rock', 'paper', or 'scissors'.")
print("To stop playing, enter 'quit'.")


playing = True

while playing:
    user_choice = input("Your choice: ")
    
    if user_choice == "quit":
        print("Thanks for playing! Goodbye!")
        
        response = input('Type "Again!": ')
        if response != 'Again!' and response != 'again!':
            print('Sorry to see you go :(')
            print('You will be remembered fondly')
            response = input('Type "Again!": ')  
            if response != 'Again!' and response != 'again!':
                print('Farewell!')
                playing = False
    
    elif user_choice in ["rock", "paper", "scissors"]:
        computer_choice = random.choice(['rock', 'paper', 'scissors'])
        print("Computer chose: " + computer_choice)

        result = play_rock_paper_scissors(user_choice, computer_choice)
        print(result)
        print()
    else:
        print("Invalid choice. Please choose 'rock', 'paper', or 'scissors' or type 'quit' to exit.")
