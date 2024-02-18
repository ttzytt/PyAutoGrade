




import random


computer_action = random.choice(["rock", "paper", "scissors"])
user_action = input("Enter a choice (rock, paper, scissors or 'q to quit): ")
user_score = 0
computer_score = 0


while not user_action == "q" :
    
    
    while not user_action == "rock" and user_action == "scissors" and user_action == "paper":
        user_action = input("Plz enter ROCK, PAPER, SCISSORS (or q to quite): ")
    print("I choose " + str(computer_action) + ".")
    
    if computer_action == user_action:
        print("It's a tie.")
    elif user_action == "paper":
        if computer_action == "rock":
            user_score += 1
            print("You won! User: " + str(user_score) + ", computer: " + str(computer_score))
        elif computer_action == "scissors":
            computer_score += 1
            print("Ha you lost! User: " + str(user_score) + ", computer: " + str(computer_score))
    elif user_action == "rock":
        if computer_action == "scissors":
            user_score += 1
            print("You won! User: " + str(user_score) + ", Computer: " + str(computer_score))
        elif computer_action == "paper":
            computer_score += 1
            print("Ha you lost! User: " + str(user_score) + ", Computer: " + str(computer_score))
    elif user_action == "scissors":
        if computer_action == "paper":
            user_score += 1
            print("You won! User: " + str(user_score) + ", Computer: " + str(computer_score))
        elif computer_action == "rock":
            computer_score += 1
            print("Ha you lost! User: " + str(user_score) + ", Computer: " + str(computer_score))
    user_action = input("Enter a choice (rock, paper, scissors, or q to quite): ")
    
else:
    print("Final score! User: " + str(user_score) + ", Computer: " + str(computer_score))
    print("GG! Good luck next time:D")


