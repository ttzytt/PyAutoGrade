import random

def roll_dice():
    
    return random.randint(1, 6)

user_money = 100

print("Welcome to Dice Roll Gambling Game!")
print("You start with $100.")
print("Place a bet on a number between 1 and 6.")
print("If the dice roll matches your bet, you win twice your bet amount!")
print("If not, you lose your bet.")
print()

while user_money > 0:
    print("You currently have $" + str(user_money) + ".")
    bet_amount = int(input("Enter your bet amount (or 0 to quit): "))
    
    
    if bet_amount == 0:
        print("Thanks for playing!")
        break
    elif bet_amount > user_money:
        print("You don't have enough money for that bet!")
        continue

    bet_number = int(input("Place your bet on a number (between 1 and 6): "))

    
    if bet_number < 1 or bet_number > 6:
        print("Invalid bet number! Please bet a number between 1 and 6.")
        continue

    result = roll_dice()
    print("The dice rolled a " + str(result) + ".")

    if bet_number == result:
        print("Congratulations! You won $" + str(6 * bet_amount) + ".")
        user_money += bet_amount
    else:
        print("Sorry, you lost $" + str(bet_amount) + ". Better luck next time!")
        user_money -= bet_amount

if user_money == 0:
    print("You're out of money! Thanks for playing!")


