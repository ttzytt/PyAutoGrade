


import random

def main():


user_choice = input("Enter 'rock', 'paper', or 'scissors': ").lower().strip()
    

if user_choice not in ['rock', 'paper', 'scissors']:
    print("Invalid choice. Please enter 'rock', 'paper', or 'scissors'.")
    
    

computer_choice = random.choice(['rock', 'paper', 'scissors'])
print(f"I choose {computer_choice}.")


if user_choice == computer_choice:
    print("We tie.")
else:
    if user_choice == 'rock':
        print("You win.") if computer_choice == 'scissors' else print("I win.")
    elif user_choice == 'paper':
        print("You win.") if computer_choice == 'rock' else print("I win.")
    elif user_choice == 'scissors':
        print("You win.") if computer_choice == 'paper' else print("I win.")

if __name__ == "__main__":
    main()


