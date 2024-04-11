




import random 

random.seed()

print("Gambling Games: Which is Bigger?") 
print("Instructions for player: In this game, you are going to gamble with the computer. The computer will randomly draw")
print("a card from the standard deck for you, and you will draw from the same deck for the computer. After that, both cards")
print("will be flipped, and the one with the bigger card wins.")
print("In this case, a standard deck means a set from number 1 to number 13.")
print("You have $100 to start with. You can bet however much you want in a round. If you win, you win the amount of the bet.")
print("If you lose, you lose that amount. If tied, money is neither won nor lost.")
print("You will be forced to quit if you lose all the money, or you can choose to quit yourself.")
print("Are you ready? Game starts now.")

money = 100 

print()
print('You have $' + str(money) + ' now.') 

again = input("Type in 's' to start the game: ") 


while again == 's':

    bet = int(input("What's the amount of money you'd like to bet?: ")) 

    computer = int(random.randint(1, 13))
    user = int(random.randint(1, 13))

    while computer == user: 
        
        computer = int(random.randint(1, 13))
        user = int(random.randint(1, 13))

    else:
        if user > computer: 
            print()
            print('Computer draw: ' + str(computer)) 
            print('Your draw: ' + str(user))
            print('You win the bet.')

            money = money + bet
            print('You have $' + str(money) + ' now.')
            
            print()
            again = input("Type in 's' if you still want to play the game, 'quit' if not: ") 
            print()

        elif user < computer: 
            print()
            print('Computer draw: ' + str(computer))
            print('Your draw: ' + str(user))
            print('You lost the bet.')

            money = money - bet
            print('You have $' + str(money) + ' left.')
            
            print()

            if money == 0 or money < 0: 
                print('Gambling is addictive, enough is enough. Bye.') 
                break
            else:
                again = input("Type in 's' if you still want to play the game, 'quit' if not: ") 
                print()

if again == 'quit': 
    print('Not losing all your money is a one-time luck. Gambling is addictive, enough is enough. Bye.') 



