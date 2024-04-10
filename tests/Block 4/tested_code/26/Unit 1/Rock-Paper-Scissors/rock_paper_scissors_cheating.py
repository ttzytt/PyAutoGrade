import random

def main():

    
    user_choice = input("Enter 'rock', 'paper', or 'scissors': ").lower().strip()

    
    if user_choice not in ['rock', 'paper', 'scissors']:
        print("Invalid choice. Please enter 'rock', 'paper', or 'scissors'.")
        return

    
    if user_choice == 'rock':
        computer_choice = 'paper'
    elif user_choice == 'paper':
        computer_choice = 'scissors'
    elif user_choice == 'scissors':
        computer_choice = 'rock'

    print(f"You choose {user_choice}.")
    print(f"I choose {computer_choice}.")                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      
    print("I win.")

if __name__ == "__main__":
    main()
