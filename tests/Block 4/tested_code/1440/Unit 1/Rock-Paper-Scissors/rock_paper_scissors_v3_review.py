


import random
possible_actions = ["rock", "paper", "scissors"]
computer_action = random.choice(possible_actions) 
                                                                        


while True: 
    user_action = input("Enter a choice (rock, paper, scissors). Enter quit if you decide not to play anymore. ")


    if user_action == "quit":
        break 
    
    cheat = random.randint(1, 10)
    if cheat == 1:
        print("Let's get rolling! ")
        if user_action == "paper" :
            print("I choose scissors. I win:p")

        elif user_action == "rock" :
            print("I chose paper. I win:)")

        elif user_action == "scissors":
            print("I choose rock. I win:D")

    
    else: 
        if computer_action == user_action:
            print("It's a tie.")
        elif user_action == "paper":
            if computer_action == "rock":
                print("You won!")
            elif computer_action == "scissors":
                print("You lost!")
        elif user_action == "rock":
            if computer_action == "paper":
                print("You lost!")
            elif computer_action == "scissors":
                print("You won!")
        elif user_action == "scissors":
            if computer_action == "paper":
                print("You won!")
            elif computer_action == "rock":
                print("You lost!")
        print("I choose " +computer_action + ".")
    

