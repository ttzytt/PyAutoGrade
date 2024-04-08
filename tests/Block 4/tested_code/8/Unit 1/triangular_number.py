


player_number = int(input("Enter a number: ")) 
triangular = player_number
print_number = player_number

while player_number > 1:
    triangular = triangular + (player_number - 1)
    player_number = player_number - 1

print(str(print_number) + "'s triangle number is: " + str(triangular))
