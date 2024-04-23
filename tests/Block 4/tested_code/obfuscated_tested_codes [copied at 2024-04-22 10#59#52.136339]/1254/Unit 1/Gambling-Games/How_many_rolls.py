


'''
This program makes the user place a bet and then guess how many rolls it takes for an 100-sided die to roll a 1. If
their guess is close enough, they win the bet, if not, they lose the bet. They can also play repeatedly. Until they
lose all their money.
'''


import random

random.seed()

user_money = 100

print("Welcome to Vivian's gameshow 'How many rolls?'")
print()
print("In this game, I will have an 100-sided die. Your job is to guess how many rolls I get before I roll a '1'.")
print()
print('''You'll start with $100, Before each round starts, you'll be able to place a bet. If your guess is within
ten rolls more or less than the actual times I roll the dice, you win and gain the money you bet.
If not, you lose the bet.''')
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
