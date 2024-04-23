


cereal_bowl = {'red' : 6, 'blue' : 5,
                'yellow' : 7, 'orange' : 7,
                'purple' : 4, 'green' : 6}
while True:
    color_combination = input("What fruit loops colors do you want to combine? (Type 'q' to quit.) ")
    
    if color_combination == 'q':
        break
    
    elif color_combination[ :5] == 'floor':
        print('Congrats! You found a new fruit loop!')
        color_combination = color_combination.split()
        
        if color_combination[1] in cereal_bowl:
            cereal_bowl[color_combination[1]] += 1
            continue
        
        else:
            cereal_bowl[color_combination[1]] = 1
            continue

    else:    
        color_combination = color_combination.split()

    num_of_combination = 0

    for i in range(len(color_combination)):
        num_of_combination += cereal_bowl[color_combination[i]]

    print(num_of_combination)
