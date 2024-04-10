






import random

def main():
    
    user_choice = input("Enter 'rock' or 'paper': ").lower()
    
    
    if user_choice not in ['rock', 'paper']:
        print("Invalid input. Please enter either 'rock' or 'paper'.")
        return

    
    computer_choice = random.choice(['rock', 'paper'])
    
    print(f"I choose {computer_choice}.")

    
    
    
    
    if user_choice == computer_choice:
        print("We tie.")
    elif user_choice == 'rock' and computer_choice == 'paper':
        print("I win.")
    elif user_choice == 'paper' and computer_choice == 'rock':
        print("You win.")
    else:
        print("Something went wrong.")  
                                        


if __name__ == "__main__":
    main()
