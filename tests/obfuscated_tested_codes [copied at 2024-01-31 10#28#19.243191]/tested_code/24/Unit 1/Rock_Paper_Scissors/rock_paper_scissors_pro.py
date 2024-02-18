



import random

user_score = 0
computer_score = 0

while True:
    user_choice = input("Enter 'rock', 'paper', or 'scissors', or 'q' to quit: ").lower()

    if user_choice == 'q':
        break
    elif user_choice not in ['rock', 'paper', 'scissors']:
        print("Invalid choice. Please try again.")
        continue

    computer_choice = random.choice(['rock', 'paper', 'scissors'])
    result = 0

    if user_choice == 'rock' and computer_choice == 'scissors':
        result = 1
    elif user_choice == 'paper' and computer_choice == 'rock':
        result = 1
    elif user_choice == 'scissors' and computer_choice == 'paper':
        result = 1
    elif user_choice == computer_choice:
        result = 0
    else:
        result = -1

    if result == 0:
        print("It's a tie! User:", user_score, "Computer:", computer_score)
    elif result == 1:
        user_score += 1 
        print("User wins! User:", user_score, "Computer:", computer_score)
    else:
        computer_score += 1
        print("Computer wins! User:", user_score, "Computer:", computer_score)

print("Final Score:")
print("User:", user_score, "Computer:", computer_score)
