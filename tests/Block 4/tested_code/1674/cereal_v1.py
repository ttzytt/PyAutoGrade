


cereal = {'red':6, 'blue':5, 'yellow':7, 'orange':7, 'purple':4, 'green':6} 


total = 0


times = int(input("How many times would you like to run this program? "))

for i in range(times):
    colors = str(input("What colors would you like? ")) 
    
    if colors not in cereal:
        print("That's not a color, try again.")

    for num in cereal: 
        if num in colors: 
            total += cereal[num] 
        
    print("There are " + str(total) + " fruit loops with those colors. ") 
    print()
    total = 0 


