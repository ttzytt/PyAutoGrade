





from random import choice, seed
seed()








def rps_score_round(player_1, player_2):
    if player_1 == "rock":
        if player_2 == "rock":
            return 0
        elif player_2 == "paper":
            return -1
        else:
            return 1
    elif player_1 == "paper":
        if player_2 == "rock":
            return 1
        elif player_2 == "paper":
            return 0
        else:
            return -1
    else:
        if player_2 == "rock":
            return -1
        elif player_2 == "paper":
            return 1
        else:
            return 0


user_score = 0
computer_score = 0
continue_playing = True


user_choice = input("Enter 'rock', 'paper', or 'scissors', or 'q' to quit: ").lower()
while user_choice != 'q':
    
    while not user_choice == 'rock' or user_choice == 'paper' or user_choice == 'scissors':
        print("Invalid Input. Try Again.")
        
        
        user_choice = input("Enter 'rock', 'paper', or 'scissors': ").lower()
    
    computer_choice =  choice(['rock', 'paper', 'scissors'])
    print("I choose " + computer_choice)

    
    result = rps_score_round(user_choice, computer_choice)
    if result == 1:
        print("You win!")
        user_score = user_score + 1
    elif result == -1:
        print("I win!")
        computer_score = computer_score + 1
    else:
        print("We tie!")

    
    print("You | " + str(user_score) + " - " + str(computer_score) + " | Me")
    
    
    user_choice = input("Enter 'rock', 'paper', or 'scissors', or 'q' to quit: ").lower()
print("Final Score: You | " + str(user_score) + " - " + str(computer_score) + " | Me")
print("Good game!")
