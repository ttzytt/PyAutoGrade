







from random import randint, seed

seed()

target_number = randint(1,10)

guess = int(input("Choose a number between 1 and 10: "))


while guess != target_number:
    
    
    if 1 <= guess and guess < target_number:
        print("That's too low!")
    
    elif 10 >= guess and guess > target_number:
        print("That's too high!")
    else:
    
        print("That's not a valid input...")
    
    guess = int(input("Choose a number between 1 and 10: "))
print("You got it!")

