


import random
import time





pause_on = True


def pause(seconds):
    if pause_on:
        time.sleep(seconds)

  

print('''
This is a number guessing gambling game.
I will think of a number between 1 and 10 (inclusive).
You will have 2 tries to guess it, and I will say if you are too high or low.
''')

pause(5)

print('''
Your balance is $100 at the start.
You can wager as much of it as you want.
If you guess the number correctly, you will win your wager.
If you guess the number incorrectly, you will lose your wager.
The game will continue until your balance is 0, or if you decide to stop.
''')

pause(5)


balance = 100

play_on = 'yes'


while balance > 0 and play_on.lower() == 'yes':
    
    wager = float(input('What is your wager? (Balance: $' + str(balance) +
                        ') '))
    while wager > balance or wager < 1: 
        pause(1)
        
        
        print("What do you mean my card's been declined? " +
              "Try it again! Invalid wager.")
        pause(1)
        wager = float(input('What is your wager? (Balance: $' + str(balance) +
                            ') '))
    
    random_number = random.randint(1, 10)
    user_guess = float(input('I have a number, what is your first guess? '))

    
    count = 1

    
    
    
    
    
    while user_guess != random_number and count < 2:
        count = count + 1
        if user_guess > random_number:
            print('Oops, too high!')
        if user_guess < random_number:
            print('Oops, too low!')
        
        user_guess = float(input('Try again! (Attempt ' + str(count) + ') '))


    
    if user_guess == random_number: 
        balance = balance + wager
        print('Nice, you got it! The number I was thinking of was ' +
              str(random_number) + '.')
        pause(3)
        print('You won $' + str(wager) + ', your balance is now $' +
              str(balance) + '.')
        pause(2)

    else: 
        balance = balance - wager
        print('Awww, so close. The number I was thinking of was ' +
              str(random_number) + '. Better luck next time!')
        print('You lost $' + str(wager) + ', your balance is now $' +
              str(balance) + '.')
        pause(2)


    
    if balance > 0:
        play_on = input("Would you like to keep playing? Type 'yes' or 'no': ")
        lost = False
    else:
        play_on = 'no'
        lost = True

pause(1)


if lost == True:
    
    print("It seems like your balance is at or below 0. " +
          "Time really flies, doesn't it?")
else:
    print("You know, 90% of gamblers quit before their big win...")

    


    
                 
