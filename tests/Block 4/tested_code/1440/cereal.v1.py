





print("I have a group of cereals with color 'red':6,'yellow':7,'purple':4,'green':6}.")
cafe = {'red':6,'yellow':7,'purple':4,'green':6}
user_answer = input('what color of cereals do u wanna count? enter "q" to quit: ')

def counting_fruitloop():
    sums = 0
    for color in colors:
        sums += cafe[color]
    return sums

while user_answer != 'q': 
    colors = user_answer.split()
    sums = counting_fruitloop()
    print(f'the sum of the color cereals u entered is:{sums}')
    user_answer = input('what color of cereals do u wanna count? enter "q" to quit: ')
                                  
    

