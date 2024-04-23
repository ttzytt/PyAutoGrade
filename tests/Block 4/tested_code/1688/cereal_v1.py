


cereals = {'red' : 6, 'blue' : 5,
                'yellow' : 7, 'orange' : 7,
                'purple' : 4, 'green' : 6}
while True:
    color_combination = input("What fruit loops colors do you want to combine? (Type 'q' to quit.) ")
    
    if color_combination == 'q':
        break
    else:
        color_combination = color_combination.split()

    num_of_combination = 0

    for i in range(len(color_combination)):
        num_of_combination += cereals[color_combination[i]]

    print(num_of_combination)
