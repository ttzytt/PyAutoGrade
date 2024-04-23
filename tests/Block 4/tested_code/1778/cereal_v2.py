


quit_input = ''
cereal = {'red': 6, 'blue': 5, 'yellow': 7, 'orange': 7, 'purple': 4, 'green': 6}

while quit_input != 'quit':
    user_input = input("Which colors would you like to search for? ")
    inputs = user_input.split()
    if inputs[0] == 'floor':
        if inputs[1] not in cereal:
            cereal[inputs[1]] = 1
        else:
            cereal[inputs[1]] += 1
    
    else:
        counter = 0
        for color in inputs:
            counter += cereal[color]
        print("There are " + str(counter) + " fruit loops with those colors.")
    quit_input = input("Enter 'quit' to stop ")


