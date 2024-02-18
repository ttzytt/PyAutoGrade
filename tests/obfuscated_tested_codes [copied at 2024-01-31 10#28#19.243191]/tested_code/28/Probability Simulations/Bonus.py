




import random
random.seed()

def tries_until_hand_is_rolled(number_1, number_2):
    count = 0
    cards_rolled = []
    random_number = random.randint(1, 52)

    while len(cards_rolled) < 2:
        if random_number == number_1:
            if random_number not in cards_rolled:
                cards_rolled.append(random_number)
                random_number = random.randint(1, 51)
        elif random_number == number_2:
            if random_number not in cards_rolled:
                cards_rolled.append(random_number)
                random_number = random.randint(1, 51)
        else:
            random_number = random.randint(1, 52)
        count += 1
    return count

def average_for_hand(num_trials):
    total = 0
    
    for _ in range(1, num_trials):
        total += tries_until_hand_is_rolled(number_1, number_2)
    
    return total/num_trials
        
num_trials = int(input('Enter how many trials you want to go through: '))
number_1 = int(input('What is the number of the first card? '))
input('What type of card is it? ')
number_2 = int(input('What is the number of the second card? '))
input('What type of card is it? ')
average_result = average_for_hand(num_trials)
print('The average amount of tries is ' + str(average_result))


    
