



bowl = {'red':6, 'blue':5, 'yellow':7, 'orange':7, 'purple':4, 'green':6}

colors = input("What colors do you want add or to search on? (Type 'quit' to stop)\n") 

while colors != 'quit': 
    colors = colors.split() 
    if colors[0] == 'floor': 
        if colors[1] not in bowl:
            bowl[colors[1]] = 1
        else:
            bowl[colors[1]] += 1 
    else:
        ans = 0
        for color in colors:
            
            if color not in bowl:
                ans = -1
                print('Color not identified.')
                print()
                break
            ans += bowl[color] 
        if ans >= 0:
            print('There are ' + str(ans) + ' fruit loops with those colors.')
            print() 

    colors = input("What colors do you want add or to search on? (Type 'quit' to stop)\n") 

print('End of the program.') 
