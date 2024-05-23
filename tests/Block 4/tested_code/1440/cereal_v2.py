






print("i have a group of cereals with color 'red':6,'yellow':7,'purple':4,'green':6.")
print("enter 'floor gold pink' will add one gold and one pink cereal to my cereal group.")
print("enter 'gold pink red' will count the sum of these 3 color cereals")

cafe = {'red':6,'yellow':7,'purple':4,'green':6}

def counting_fruitloop_floor():
    colors = input('What color do you wanna count or what color do you wanna add? ').split()
    sums = 0 
    if colors[0] == 'floor':
        for i in range(1,len(colors)):
            if colors[i] in cafe:
                cafe[colors[i]] = cafe[colors[i]] + 1
            else:
                cafe[colors[i]] = 1
    else:
        for color in colors:
            sums += cafe[color] 
        print('the sum for these color cereals is:' + str(sums))
    print(cafe)
    return cafe

def main():
    user_quit = input('do u wanna quit? Enter "yes" or "no"')
    
    while user_quit != 'yes':
        cafe = counting_fruitloop_floor()
        user_quit = input('do u wanna quit?  Enter "yes" or "no"')
        

if __name__ == "__main__":
    main()
