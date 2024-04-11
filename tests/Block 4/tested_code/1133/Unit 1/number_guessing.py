import random


secret_number = random.randint(1, 10)


attempts = 0

while True:
    
    guess = int(input("Guess the number between 1 and 10: "))
    
    
    attempts += 1
    
    
    if guess == secret_number:
        print("Congratulations! You guessed the number " + str(secret_number) + " correctly in " + str(attempts) + " attempts.")
        break  
    elif guess < secret_number:
        print("Too low, Try again.")
    else:
        print("Too high, Try again.")
