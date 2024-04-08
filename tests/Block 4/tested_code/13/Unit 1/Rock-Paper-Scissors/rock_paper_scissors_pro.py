import random


total_score = 0

print("Welcome to Rock-Paper-Scissors Pro!")

while True:
    user_choice = input("Enter 'rock', 'paper', or 'scissors', or 'q' to quit: ").lower()

    if user_choice == 'q':
        break  

    
    if user_choice not in ['rock', 'paper', 'scissors']:
        print("Invalid input. Please try again.")
        continue

    
    computer_choice = random.choice(['rock', 'paper', 'scissors'])

    print(f"You chose {user_choice}. Computer chose {computer_choice}.")

    
    if user_choice == computer_choice:
        print("It's a tie!")
    elif (
        (user_choice == 'rock' and computer_choice == 'scissors') or
        (user_choice == 'scissors' and computer_choice == 'paper') or
        (user_choice == 'paper' and computer_choice == 'rock')
    ):
        print("You win this round!")
        total_score += 1
    else:
        print("Computer wins this round!")
        total_score -= 1

    
    print(f"Total Score: {total_score}")

print("Thanks for playing Rock-Paper-Scissors Pro!")
