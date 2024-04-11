


import random
random.seed()





def tries_until_duplicate_birthday():
    
    birthday_list = []
    
    while True:
        
        random_day = random.randint(1, 365)
        
        if random_day not in birthday_list:
            birthday_list.append(random_day)
            
        else:
            break

    return len(birthday_list)


def average_until_duplicate_birthday(num_trials):
    
    total = 0
    
    for i in range(num_trials):
        total += tries_until_duplicate_birthday()

    return total / num_trials





num_trials = int(input("Enter the number of trials: "))
print(average_until_duplicate_birthday(num_trials))







