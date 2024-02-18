



import random


print('Welcome to Dice Roll!')
print()
print('I will roll a dice and you can bet your money')
print('on guessing the number I roll correctly.')
print('If you guess correctly, you win 2x your bet!')
print('But if you get it wrong, you lose your bet.')
print()

balance = 100

while balance > 0:
    print(f'Your current balance is {balance}')
    
    
    bet = -1
    while bet < 0 or bet > balance:
        bet_input = input('Place your bet (or enter 0 to quit): ')
        if bet_input.isdigit():
            bet = int(bet_input)

        
        elif bet < 0 or bet > balance:
                print('Invalid bet amount. Please enter a valid amount.')
        
        
    
    if bet == 0:
        print('Thanks for playing! Your final balance is', balance)
        break
    
    
    dice_roll = random.randint(1, 6)
    
    
    guess = 0
    while guess < 1 or guess > 6:
        guess_input = input('Guess the number (1-6): ')
        if guess_input.isdigit():
            guess = int(guess_input)
            if guess < 1 or guess > 6:
                print('Invalid guess. Please guess a number between 1 and 6.')
        else:
            print('Invalid input. Please enter a valid number.')
    
    print(f'The dice rolled: {dice_roll}')
    
    
    if guess == dice_roll:
        print(f'Congratulations! You guessed correctly. You win {2 * bet} fake dollars!')
        balance = balance + 2 * bet
    else:
        print(f'Sorry, you guessed wrong. You lose {2 * bet} fake money.')
        balance = balance - bet

    
    

print('Game over! Your balance reached 0.')    
