


quit_input = ''
while quit_input != 'quit':
    cereal = {'red': 6, 'blue': 5, 'yellow': 7, 'orange': 7, 'purple': 4, 'green': 6}
    user_input = input("Which colors would you like to search for? ")
    inputs = user_input.split()
    counter = 0
    for color in inputs:
        counter += cereal[color]
    print("There are " + str(counter) + " fruit loops with those colors.")
    quit_input = input("Enter 'quit' to stop ")


