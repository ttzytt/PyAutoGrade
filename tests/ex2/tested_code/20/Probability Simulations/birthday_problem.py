




import random

random.seed()















def tries_until_duplicate_birthday():
    birthdays = []
    
    birthday = random.randint(1, 365)
    while birthday not in birthdays:
        
        birthdays.append(birthday)
        birthday = random.randint(1, 365)
    
    return len(birthdays)





def average_until_duplicate_birthday(num_trials):
    total = 0
    for i in range(1, num_trials):
        total += tries_until_duplicate_birthday()
    return total/num_trials



num_trials = int(input('Enter how many trials you want to go through: '))
average_result = average_until_duplicate_birthday(num_trials)
print(f'The average amount of trials until you get a duplicate birthday is {average_result}')
    
    

        
