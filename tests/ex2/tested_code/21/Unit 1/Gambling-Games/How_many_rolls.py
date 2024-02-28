





import random

random.seed()

user_money = 100

print("Welcome to Vivian's gameshow 'How many rolls?'")
print()
print("In this game, I will have an 100-sided die. Your job is to guess how many rolls I get before I roll a '1'.")
print()
print()
print() 

user_start = input("Please type 'start' to start the round, or 'quit' to exit the game: ")



while user_start == 'start':  

    dice = random.randint(1, 100)

    print()
    bet = int(input('How much money will you bet for this round? '))
    print()
    print("Great choice! Let the games begin...")
    print()
    user_guess = int(input("How many rolls till I get a 1? "))

    rolls = 0

    computer_cheat_chance = random.randint(1,20)

    if computer_cheat_chance == 10:
        print("Oh no! I'm sorry for your loss. :(")
        user_money = user_money - bet
        print('Your total now is $' + str(user_money) + '.')

    else:

        while dice != 1: 
            rolls = rolls + 1
            dice = random.randint(1, 100)

        if dice == 1:
            if user_guess < (10 + rolls) and user_guess > (rolls - 10):
                print('Well done! You just won $' + str(bet) + '.')
                user_money = user_money + bet
                print('Your total now is $' + str(user_money) + '.')
            else:
                print("Oh no! I'm sorry for your loss. :(")
                user_money = user_money - bet
                print('Your total now is $' + str(user_money) + '.')



        if user_money <= 0:
            print("Oops, too invested? Go outside and touch some grass loser!")
            break 


        print()

        print ('Would you like to start the next round? ')
        user_start = input("Type 'start' to start a new round, type 'quit' to exit the game: ")

    


            
            
        
if user_start != 'start':
    print("Sorry to see you go :'(, Come back next time!")
