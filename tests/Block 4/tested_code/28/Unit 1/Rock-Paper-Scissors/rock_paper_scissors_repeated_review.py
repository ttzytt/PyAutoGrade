


from random import choice

user_choice = input("Choose 'rock', 'paper', 'scissors' or 'quit' to quit: ").lower()

while not user_choice == "quit":
    
    computer_choice = choice(['rock', 'paper', 'scissors'])
    print("I choose " + computer_choice)

    if computer_choice == "rock":
        if user_choice == "rock":
            print("We tie.")
        if user_choice == "paper":
            print("You win.")
        if user_choice == "scissors":
            print("I win.")
    if computer_choice == "paper":
        if user_choice == "rock":
            print("I win.")
        if user_choice == "paper":
            print("We tie.")
        if user_choice == "scissors":
            print("You win.")
    if computer_choice == "scissors":
        if user_choice == "rock":
            print("You win.")
        if user_choice == "paper":
            print("I win.")
        if user_choice == "scissors":
            print("We tie.")

    
    
    
    
    user_choice = input("Choose 'rock', 'paper', 'scissors' or 'quit' to quit: ").lower()
print("See you later :)")


