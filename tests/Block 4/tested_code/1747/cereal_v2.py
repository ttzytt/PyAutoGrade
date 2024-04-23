





num_fruit_loops = {'red' : 6,
                   'blue' : 5,
                   'yellow' : 7,
                   'orange' : 7,
                   'purple' : 4,
                   'green' : 6,
                   }


print(num_fruit_loops)
print('Currently, these are the fruit loops in the bowl.')
print("If you pick up one fruit loop from the floor, enter 'floor color'.")
print("You can also paint a new color yourself! If you do, enter 'floor color'.")
print("You can also ask for total count of one or multiple color(s) by entering the color(s).")
print('If you input multiple colors, divide them with space.')
colors_input = input('What would you like to do?: ')


while colors_input != 'Quit' and colors_input != 'quit':

    colors = colors_input.split() 

    if colors[0] == 'floor':

        if colors[1] in num_fruit_loops:
            


    

    total_count = 0

    for color in colors: 
        total_count += num_fruit_loops[color]

    print('There are ' + str(total_count) + ' fruit loops with those colors.')
    
    print("Enter 'quit' if you don't want to start again.")
    colors_input = input('What color(s) of cereal would you like to add together?: ')

print('Bye.')
