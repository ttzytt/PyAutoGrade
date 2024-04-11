


import random

random.seed()


random_number = random.randint(1, 10)


user_guess = int(input('I have thought of a number between 1 and 10 (inclusive), ' +
                       'try to guess it! '))


attempts = 1

while user_guess != random_number: 
    
    if user_guess > random_number:
        print('Oops, too high!')
    if user_guess < random_number:
        print('Oops, too low!')

    
    
    
    user_guess = int(input('Try again! '))

    attempts = attempts + 1


print('Nice, you got it! The number I was thinking of was ' +
      str(random_number) + '. You took ' + str(attempts) + ' attempt(s)!')
                 
