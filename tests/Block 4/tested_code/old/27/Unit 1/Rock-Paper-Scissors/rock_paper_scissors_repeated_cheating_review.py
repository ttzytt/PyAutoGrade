




import random
random.seed()
cheat_number = random.randint(1, 10)



if cheat_number == 5:
    user = input("Enter 'rock' 'paper' or 'scissors' : ")


    if (user == "rock"):
        computer_selection = "paper"
        print("I choose " + computer_selection)
        if(computer_selection == "paper"):
            print("I win.")

    elif (user == "paper"):
        computer_selection = 'scissors'
        if(computer_selection == "scissors"):
            print("I win.")

    elif (user == "scissors"):
        computer_selection = "rock"
        print("I choose " + computer_selection)
        if(computer_selection == "rock"):
            print("I win.")




else:
    user = input("Enter 'rock' 'paper' or 'scissors' : ")

    computer_selection_list = ['rock', 'paper', 'scissors']


    computer_selection = random.choice(computer_selection_list)

    print("I choose " + computer_selection)

    if (user == "rock"):
        if(computer_selection == "rock"):
            print("We tie.")
        elif(computer_selection == "paper"):
            print("I win.")
        elif(computer_selection == "scissors"):
            print("I lose.")

    elif (user == "paper"):
        if(computer_selection == "rock"):
            print("You win.")
        elif(computer_selection == "paper"):
            print("We tie.")
        elif(computer_selection == "scissors"):
            print("I win.")

    elif (user == "scissors"):
        if(computer_selection == "rock"):
            print("You win.")
        elif(computer_selection == "paper"):
            print("I win.")
        elif(computer_selection == "scissors"):
            print("We tie.")



