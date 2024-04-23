





cereal = {'red':6, 'blue':5, 'yellow':7, 'orange':7, 'purple':4, 'green':6}


print('I have a bowl of fruit loops. There are red, orange, yellow, green, blue, and purple')


user_color_choice = input('what color(s) do you want to know number of fruit loops of? \n'
                          '(ex. "red orange yellow", "blue"): ')


seperate_colors = user_color_choice.split()
cereal_count = 0 


for color in seperate_colors:
    cereal_count += cereal[color] 


print('There are ' + str(cereal_count) + ' fruit loops with those colors')
        
    
