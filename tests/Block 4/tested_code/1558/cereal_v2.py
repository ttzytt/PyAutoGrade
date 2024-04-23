






cereal = {'red':6, 'blue':5, 'yellow':7, 'orange':7, 'purple':4, 'green':6}


print('I have a bowl of fruit loops. There are red, orange, yellow, green, blue, and purple')
print('You can select any number of colors and get the amount of those colors in the bowl')
print('You can also write "floor" followed by a color and add a new color or add to an'
      'existing color to the bowl and get the number of that color in the bowl')
print()


user_color_choice = input("input or 'quit' (ex. 'red blue yellow', 'floor pink'): ")

while user_color_choice[:4] != 'quit': 
        
    if user_color_choice[:5] != 'floor':
        
        seperate_colors = user_color_choice.split()
        cereal_count = 0 


        for color in seperate_colors:
            cereal_count += cereal[color] 

        
        print('There are ' + str(cereal_count) + ' fruit loops with those colors')

    else:
        floor_color = user_color_choice.split()
        added_color = floor_color[1]
        if added_color in cereal:
            cereal[added_color] += 1
        else:
            cereal[added_color] = 1 
            
    print(cereal[added_color], added_color) 
    print()
    user_color_choice = input("input or 'quit' (ex. 'red blue yellow', 'floor pink'): ")
print('bye :(')
