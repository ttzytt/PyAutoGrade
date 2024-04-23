import random




def play_game():
    print("Welcome to the Complex Number Guessing Game!")
    print("Try to guess the mysterious number. I'll give you hints to help you.")

    lower_limit = int(input("Enter the lower limit for the range: "))
    upper_limit = int(input("Enter the upper limit for the range: "))
    
    secret_number = random.randint(lower_limit, upper_limit)
    
    print (f"I've selected a number between {lower_limit} and {upper_limit}. Let's get started!")


while True:

    if guess == secret_number:
        print("Congratulations! You guessed the correct number.")

    elif guess < secret_number:
        print("Too low! Try again.")
    else:
        print("Too high! Try again.")
