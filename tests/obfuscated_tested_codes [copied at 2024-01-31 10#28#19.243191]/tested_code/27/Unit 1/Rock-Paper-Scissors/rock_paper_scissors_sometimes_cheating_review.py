


import random
possible_actions = ["rock", "paper", "scissors"]






while True:
    user_action = input("Enter a choice (rock, paper, scissors): ")
    if user_action == "scissors":
        
        computer_action = random.choices(possible_actions,weights=(43, 28.5, 28.5))[0] 

        
        print("I choose " + computer_action + ".")

        
        if computer_action == "paper":
            print("You won!")
        elif computer_action == user_action:
            print("It's a tie.")
        elif computer_action == "rock":
            print("I won!")
    
    elif user_action == "paper":
        computer_action = random.choices(possible_actions,weights=(28.5, 28.5, 43))[0] 
        print("I choose " + computer_action + ".")
        if computer_action == "paper":
            print("It's a tie.")
        elif computer_action == "scissors":
            print("I won!.")
        elif computer_action == "rock":
            print("You won!")
            
    elif user_action == "rock":
        computer_action = random.choices(possible_actions,weights=(28.5, 43, 28.5))[0]
        print("I choose " + computer_action + ".")
        if computer_action == "rock":
            print("It's a tie.")
        elif computer_action == "paper":
            print("I won!.")
        elif computer_action == "scissors":
            print("You won!")








