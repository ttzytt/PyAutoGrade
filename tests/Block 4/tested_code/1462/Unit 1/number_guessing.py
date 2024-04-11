


import random
random.seed()


program_choose = random.randint(1,10)
user_guess = int(input('Guess the number between 1 to 10: '))


while user_guess != program_choose:

    if user_guess > program_choose:
        print('Too high!')
    elif user_guess < program_choose:
        print('Too low!')

    
    user_guess = int(input('Guess again: '))

print() 
print('You guessed it right! The number is ' + str(program_choose) + '.') 
