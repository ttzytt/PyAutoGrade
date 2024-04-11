import random
money = 100

while money > 0:
    
    print(f"You have ${money}")

    bet = int(input("Enter your bet (up to your total amount): $"))

    choice = input("Choose heads or tails: ")

    
    coin_result = random.choice([0, 1])

    if (choice == 'heads' and coin_result == 0) or (choice == 'tails' and coin_result == 1):
        print(f"You guessed correctly! You won ${bet}")
        money += bet  
    else:
        print(f"Sorry, you guessed incorrectly. You lost ${bet}")
        money -= bet  


print("Game over. You're out of money.")
