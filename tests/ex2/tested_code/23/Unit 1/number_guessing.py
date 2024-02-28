


import random
random.seed()


target = random.randint(1, 10)
guess = int(input("Guess a number from 1 - 10: "))


while guess != target: 
    if guess < target:
        guess = int(input("Too low. Guess Again: "))
    elif guess > target:
        guess = int(input("Too high. Guess Again: "))

print("Correct!")
