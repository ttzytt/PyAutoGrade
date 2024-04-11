







import random
random.seed()

def tries_until_duplicate_birthday():
        
    
    birthday_list = []
    possible_birthday = random.randint(1, 365)

    
    while possible_birthday not in birthday_list:
        birthday_list.append(possible_birthday)
        possible_birthday = random.randint(1, 365)

    
    return len(birthday_list) + 1




def average_until_duplicate_birthday(num_trials):

    sum_of_tries = 0
    
    for _ in range(num_trials):
        sum_of_tries += tries_until_duplicate_birthday()

    return sum_of_tries/num_trials



num_trials_input = int(input('How many times do you want to test: '))

result = average_until_duplicate_birthday(num_trials_input)

print("The average number of days it took until a duplicate birthday was: " + str(result))


