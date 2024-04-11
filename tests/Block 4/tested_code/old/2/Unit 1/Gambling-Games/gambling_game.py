




import random
money = 100


print("Welcome to Maya's coin flip game!")
print('You can choose between heads or tails, and how much you want to bet!')
print('The game will end when you lose all of your money, or enter quit at the end of a round.')


while money > 0:
    
    
    print('You have ' + str(money) + ' dollars.')

    
    bet = int(input("Enter your bet (up to your total amount): "))
    choice = input("Choose heads or tails: ")

    
    coin_result = random.choice([0, 1])

    
    if (choice == 'heads' and coin_result == 0) or (choice == 'tails' and coin_result == 1):
        print('You guessed correctly! You won ' + str(bet) + ' dollars!')
        money = money + bet  

    
    else:
        print(f"Sorry, you guessed incorrectly. You lost ${bet}")
        money = money - bet  

    
    
    quit_choice = input('Would you like to continue (type quit to exit)? ')
    if quit_choice == 'quit':
        print('Thanks for playing!')
        break 


print("Game over.")


          
