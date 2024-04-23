



cafe = {'red':6,'yellow':7,'purple':4,'green':6}
user_answer = input('what color of cereals do u wanna count? enter "q" to quit: ')

def counting_fruitloop():
    sums = 0
    for color in colors:
        sums += cafe[color]
    return sums

while user_answer != 'q': 
    colors = user_answer.split()
    counting_fruitloop()
    user_answer = input('what color of cereals do u wanna count? enter "q" to quit: ')
    

