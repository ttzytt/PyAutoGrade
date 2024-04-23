while True :
    user_choise = input("Chose rock, paper or scissors. ")
    if user_choise == "rock" :
        print ("You chose rock")
        print ("The computer chose paper")
        print ("The computer wins!")
    
    elif user_choise == "scissors" :
        print ("You chose scissors")
        print ("The computer chose rock")
        print ("The computer wins!")
    
    elif user_choise == "paper" :
        print ("You chose paper")
        print ("The computer chose scissors")
        print ("The computer wins!")
    else :
        print ("Try again. Please chose rock, paper or scissors.")
    
    play_again = input("Do you want to play again? (yes/no): ").lower()
    if play_again != "yes":
        break
print ("See you next time")
