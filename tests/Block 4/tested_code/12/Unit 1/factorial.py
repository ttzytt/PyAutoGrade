




player_number = int(input("Enter a number:"))
factorial = player_number


while player_number > 1:
    factorial = factorial * (player_number - 1)
    player_number = player_number - 1
print("The factorial of your number is: " + str(factorial))
