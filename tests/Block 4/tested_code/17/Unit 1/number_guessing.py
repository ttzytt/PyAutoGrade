



import random


target_number = random.randint(1, 10)  


response = input('Guess the number between 1 and 10: ')
response = int(response)


while response != target_number:
    if response > target_number:
        print("Your guess is too high, maybe you should try again...")
    else:
        print("Your guess is too low. Try again!")
    response = int(input('Guess the number between 1 and 10: '))


print('You got it!')
