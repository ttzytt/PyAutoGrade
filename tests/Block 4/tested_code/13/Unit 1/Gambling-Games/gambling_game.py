

import random


total_money = 100

print("Welcome to the Dice Rolling Gambling Game!")
print("You start with $100. Bet wisely!")

while total_money > 0:
    print(f"\nYou currently have ${total_money}.")

    
    while True:
        try:
            bet = int(input("Place your bet (1 to your total money or 0 to quit): "))
            if bet < 0 or bet > total_money:
                print("Invalid bet. Please bet between 1 and your total money.")
            else:
                break
        except ValueError:
            print("Invalid input. Please enter a number.")

    
    if bet == 0:
        print("Thanks for playing! You're leaving with $" + str(total_money) + ".")
        break

    
    dice_roll = random.randint(1, 6)
    print(f"The dice rolled: {dice_roll}")

    
    if dice_roll == 1:
        print("You lost! Better luck next time.")
        total_money -= bet
    elif dice_roll == 6:
        print("Congratulations! You won!")
        total_money += bet
    else:
        print("It's a tie. You get your bet back.")

if total_money <= 0:
    print("You've run out of money. Thanks for playing!")
