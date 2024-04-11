


import random
import time

random.seed()


pause_on = True


def pause(seconds):
    if pause_on:
        time.sleep(seconds)

  

print()

pause(5)

print()

pause(5)


balance = 100

play_on = 'yes'


while balance > 0 and play_on.lower() == 'yes':
    
    wager = float(input('What is your wager? (Balance: $' + f"{balance:.2f}" +
                        ') '))
    while wager > balance or wager <= 0: 
        pause(1)
        print("What do you mean my card's been declined? " +
              "Try it again! Invalid wager.")
        pause(1)
        wager = float(input('What is your wager? (Balance: $' +
                            f"{balance:.2f}" + ') '))

    
    random_number = random.randint(1, 10)

    
    user_guess = float(input('I have a number, what is your first guess? '))
    if user_guess != random_number: 
        if user_guess > random_number:
            print('Oops, too high!')
        elif user_guess < random_number:
            print('Oops, too low!')
        user_guess = float(input('Try again! (Attempt 2) '))


    
    if user_guess == random_number: 
        balance = balance + wager
        print('Nice, you got it! The number I was thinking of was ' +
              str(random_number) + '.')
        pause(3)
        print('You won $' + f"{wager:.2f}" + ', your balance is now $' +
              f"{balance:.2f}" + '.')
        pause(2)

    else: 
        balance = balance - wager
        print('Awww, so close. The number I was thinking of was ' +
              str(random_number) + '. Better luck next time!')
        print('You lost $' + f"{wager:.2f}" + ', your balance is now $' +
              f"{balance:.2f}" + '.')
        pause(2)


    
    if balance > 0:
        play_on = input("Would you like to keep playing? Type 'yes' or 'no': ")
        lost = False
    else:
        play_on = 'no'
        lost = True

pause(1)


if lost == True:
    print("It seems like your balance is at 0. " +
          "Time really flies, doesn't it?")
else:
    print("You know, 90% of gamblers quit before their big win...")

    


    
                 
