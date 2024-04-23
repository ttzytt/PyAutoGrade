



import random

random.seed()


guess_number = random.randint(1, 1000) 
print('Guess the number! The number is between 1 and 1000. '
      + 'You only have 8 chances to find the actual number.')

if guess_number < 100:
    digit_sum = (guess_number - guess_number % 10)/ 10 + guess_number % 10
elif guess_number < 1000:
    digit_sum = ((guess_number - guess_number % 100)/ 100
                 + (guess_number % 100 - guess_number % 10)/ 10 + guess_number % 10)

digit_sum = int(digit_sum)

if digit_sum != 0:
    print('Hint: The sum of all the digits in the number is ' + str(digit_sum) + '.')

print() 

chance = 8 
guess_input = int(input('Enter your guess: '))


whether_correct = 'No' 
while whether_correct == 'No' and chance > 0: 
    
    if guess_input == guess_number:
        print('Correct! You get it!')
        whether_correct = 'Yes' 

     
    elif guess_input < guess_number:
        print('Your guess is too low.')
        chance = chance - 1
        print('You now only have ' + str(chance) + ' chances.')
        print() 
        if chance != 0:
            guess_input = int(input('Guess again: '))
        

    
    else:
        print('Your guess is too high.')
        chance = chance - 1
        print('You now only have ' + str(chance) + ' chances.')
        print() 
        if chance != 0:
            guess_input = int(input('Guess again: '))
        

if chance == 0: 
    print('You fail the number guessing game!')

