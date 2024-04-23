




import random
random.seed()
player = int(100)


print("Welcome to Gambling Game!")
print("Here you will play a game called Rock, Paper, Scissors")
print("You will play with the computer which make choices randomly.")
print("You are going to start with $100 and you can decide how much you bet each round.")
print("The money you bet shouldn't bigger than the money you have")
print("Now, game start!")
print()


attitude = str(input("Are you ready? "))


while attitude == "Yes".lower() and player > 0:
    computer_choice = random.choice(['rock', 'paper', 'scissors'])
    print('Our computer has made its choice!')
    bet_amout = int(input('How much would you want to bet?'))
    print('You now have ' + str(player - bet_amout) + ' dollars.')
    print()
    choice = str(input("Enter 'rock', 'paper' or 'scissors': "))
    print('The computer choose ' + computer_choice)
    if ((choice == 'rock' and computer_choice == 'paper')
        or (choice == 'paper' and computer_choice == 'scissors')
        or (choice == 'scissors' and computer_choice == 'rock')):
        print("What a pitty, you'll won next time.")
        player = int(player - bet_amout)
        print("You still have " + str(player))
        print()
            
    elif ((choice == 'paper' and computer_choice == 'rock')
        or (choice == 'scissors'and computer_choice == 'paper')
        or (choice == 'rock' and computer_choice == 'scissors')):
        print('Congratuation! You won!')
        player = int(player + bet_amout)
        print("You got " + str(player))
        print()
    
    else:
        print('We tie! Why not try again?')
        print("You got " + str(player))
        print()
    attitude = str(input("Would you want to try again?"))
    
print("Welcome again to.")
