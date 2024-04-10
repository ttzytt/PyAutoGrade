


user_number = int(input("Please enter a number."))
triangle_number = user_number
while user_number > 1:
    triangle_number = (triangle_number * (user_number + 1)) / 2
    user_number = 0  

print('The triangular number of your number is ' + str(round(triangle_number)))
