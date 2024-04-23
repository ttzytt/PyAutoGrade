



import random 

random.seed()


computer = int(random.randint(1, 10)) 

user = int(input('I have a number between 1 and 10. Guess what it is: ')) 


while user > computer or user < computer: 

    if user > computer:
        print('This is too high. Try again.')

    elif user < computer:
        print('This is too low. Try again.')

    user = int(input('Your guess: '))


print('Yay! You got it right.') 



