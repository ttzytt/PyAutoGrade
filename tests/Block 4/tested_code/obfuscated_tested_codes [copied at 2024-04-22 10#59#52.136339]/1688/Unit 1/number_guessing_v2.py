


import random
random.seed()


print("Welcome to Number Guessing 2.0!")
print("I'll pick a random integer between 1 and 100. Your job is to guess it.")
print("I'll give you a hint if your first guess is wrong.")

target = random.randint(1, 100)   
num_of_guesses = 0   
hint_given = False   


while True:
    guess = input("\nEnter your guess: ")

    
    if not guess.isdigit():
        print("Invalid input. Try again.")
        continue

    
    guess = int(guess)
    num_of_guesses += 1

    
    if guess == target:
        print(f"🎉Correct! You've guessed it in {num_of_guesses} tries.")
        break

    
    if not hint_given:
        n = target
        sum_digits = 0

        
        while n > 0:
            sum_digits += n % 10
            n //= 10

        
        print(f"💡Hint: Sum of digits = {sum_digits}")
        hint_given = True

    
    if guess < target:
        print("🔻Too low!")
    else:
        print("🔺Too high!")
