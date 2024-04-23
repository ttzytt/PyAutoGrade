




cereal = {'red':6, 'blue':5, 'yellow':7, 'orange':7, 'purple':4, 'green':6}


total = 0

times = int(input("How many times would you like to run this program? "))

for _ in range(times):
    
    colors = input("What colors would you like? ").split()

    if "floor" in colors:
        for num in cereal: 
            if num == colors[1]: 
                total += cereal[num] + 1 
                
    elif colors not in cereal:
        for color in colors: 
            if color not in cereal:
                if "floor" in colors:
                    total += 2
                else:
                    total += 1
        
    else:
        for num in cereal: 
            if num in colors: 
                total += cereal[num]
                
        
    print("There are " + str(total) + " fruit loops with those colors. ") 
    print()
    total = 0 


