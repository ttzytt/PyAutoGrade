





num_fruit_loops = {'red' : 6,
                   'blue' : 5,
                   'yellow' : 7,
                   'orange' : 7,
                   'purple' : 4,
                   'green' : 6,
                   }


print('There are red, blue, yellow, orange, purple, and green fruit loops.')
print('If you input multiple colors, divide them with space.')
colors_input = input('What color(s) of cereal would you like to add together?: ')


while colors_input != 'Quit' and colors_input != 'quit':

    colors = colors_input.split() 

    total_count = 0

    for color in colors: 
        total_count += num_fruit_loops[color]

    print('There are ' + str(total_count) + ' fruit loops with those colors.')
    
    print("Enter 'quit' if you don't want to start again.")
    colors_input = input('What color(s) of cereal would you like to add together?: ')

print('Bye.')
