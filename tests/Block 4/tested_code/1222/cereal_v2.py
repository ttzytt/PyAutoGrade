


cereal_key = {'purple':4, 'blue':5, 'red':6, 'green':6, 'yellow':7, 'orange':7}

run_loop = True
while run_loop == True:
    user_input = input("What color(s) do you want to count? ('quit' to quit)")

    if user_input == 'quit':
        print("Sad to see you go ˙◠˙")
        run_loop = False
    else:
        colors = user_input.split()
        cereal_count = 0
        count = 0 
        while count < len(colors):
            
            color = colors[count]
            if color == 'floor':
                count += 1
                if count < len(colors):
                    next_color = colors[count]
                    if next_color in cereal_key:
                        cereal_key[next_color] += 1
                    else:
                        cereal_key[next_color] = 1
            
            elif color in cereal_key:
                cereal_count += cereal_key[color]
            
            else:
                cereal_key[color] = 1
                cereal_count += 1
            count += 1
        print('There are ' + str(cereal_count) + ' fruit loops with those colors')

