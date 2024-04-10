







from random import choice, seed
seed()

user_choice = input("Choose 'rock', 'paper', 'scissors' or 'quit' to quit: ").lower()

while not user_choice == "quit":
    
    computer_choice = choice(['rock', 'paper', 'scissors'])
    print("I choose " + computer_choice)

    
    if computer_choice == "rock":
        if user_choice == "rock":
            print("We tie.")
        elif user_choice == "paper":
            print("You win.")
        elif user_choice == "scissors":
            print("I win.")
        else:
            print("But you chose an invalid input :(")
    elif computer_choice == "paper":
        if user_choice == "rock":
            print("I win.")
        elif user_choice == "paper":
            print("We tie.")
        elif user_choice == "scissors":
            print("You win.")
        else:
            print("But you chose an invalid input :(")
    else:
        if user_choice == "rock":
            print("You win.")
        elif user_choice == "paper":
            print("I win.")
        elif user_choice == "scissors":
            print("We tie.")
        else:
            print("But you chose an invalid input :(")

    
    print()
    
    
    
    
    
    user_choice = input("Choose 'rock', 'paper', 'scissors' or 'quit' to quit: ").lower()
    
print("See you later :)")
