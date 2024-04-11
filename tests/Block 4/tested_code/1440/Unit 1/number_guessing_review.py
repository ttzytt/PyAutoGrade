



import random
random.seed()







answer = 10
user_action = int(input("Guess what number from 1-10 did I choose:D? "))

while int(user_action) > int(answer):
        print("You answer is too high!")
        user_action = input("Guess what number from 1-10 did I choose:D? ")
while int(user_action) < int(answer):
        print("You answer is too low!")
        user_action = input("Guess what number from 1-10 did I choose:D? ")
if int(user_action) == int(answer):
        print("You got it!")       


