






import random

random.seed()

computer_choice = int(random.choice(['1', '2', '3', '4', '5', '6', '7', '8', '9', '10']))


guess = int(input('Enter a number: '))


while guess != computer_choice: 
    if guess < computer_choice:
        print('too low, try again!')
    elif guess > computer_choice:
        print('too high, try again!')
    guess = int(input('Enter a number:'))

print('congratuation!')
