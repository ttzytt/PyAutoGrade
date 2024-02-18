





import random
random.seed()

generated_number = random.randint(1, 10)

guess_number = int(input("Try to guess the number between 1-10: "))



while guess_number > 10 or guess_number < 1:
	guess_number = int(input("Please enter a number between 1-10: "))

while generated_number != guess_number:
    if guess_number <=10 and guess_number >= 0:
        if guess_number > generated_number:
            print("too high")
            guess_number = int(input("Try to guess the number between 1-10: "))
        if guess_number < generated_number:
            print("too low")
            guess_number = int(input("Try to guess the number between 1-10: "))
        if guess_number == generated_number:
            print("You Are Correct")






