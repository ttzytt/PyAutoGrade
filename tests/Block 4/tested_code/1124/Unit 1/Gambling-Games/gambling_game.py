


'''
This code will provide $100 to the player, ask how much they want to bet on a coin toss
(heads or tails).  They win the amount if they bet correctly and lose the amount if
they bet incorrectly.
There are blank lines that print nothing to help the readability when you run
the code.
'''

import random

random.seed()



print('Welcome to HEADS or TAILS run by Derek Li.')
print()
print('You have $100.')
print()
print('You will bet however much money you want.')
print()
print('I will flip a coin and you will guess if it is heads or tails.')
print()
print('If you guess it correctly, you earn that amount of money.')
print()
print('If you guess it incorrectly, you will lose that amount of money.')
print()

money = 100

play_again = 'yes'

while play_again == 'yes' and money > 0:
    
    print('You have', money, 'dollars left.')
    print()
    
    
    bet = int(input('How many dollars do you want to bet? '))
    print()


    
    user_guess = input('What is your guess, heads or tails? ')
    print()

    
    cheat = random.randint(1,20)

    
    if cheat == 1:
        if user_guess == 'heads':
            coin_flip = 'tails'
            print('The flip was tails.')
            print()

        elif user_guess == 'tails':
            coin_flip = 'heads'
            print('The flip was heads.')
            print()
            
        
        money = money - bet
        print('Too bad, you guessed wrong. You lose', bet, 'dollars.')
        print()

    
    else:
        
        coin_flip = random.choice(['heads', 'tails'])
        
        print('The flip was ' + coin_flip + '.')
        print()

        
        
        if coin_flip == user_guess:
            money = money + bet
            print('Wow, you guessed right.  You win ', bet, ' dollars.')
            print()

        elif coin_flip != user_guess:
            money = money - bet
            print('Too bad, you guessed wrong. You lose ', bet, ' dollars.')
            print()

    
    
    
    if money > 0:
        print('Do you want to play again?')
        print()
    
        play_again = input("Type 'yes' to play again or 'no' to quit. ")
        print()


        
        
        if play_again == 'no':
            print('''Are you sure you want to quit? 99% of gamblers quit before
hitting big.''')
            print()
            play_again = input("Type 'yes' to play again or 'no' to quit. ")
            print()
    
    
    elif money <= 0:
        print("You don't have any money left!")
        print()
        print("You can't play anymore.")
        print()
        
    
print('Bye Bye!')  
        
        

    
    

    
