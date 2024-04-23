




import random

random.seed()
'''
Asks for user to input the amount of trials they want to
generate birthdays until 2 people have a duplicate birthday
It will then divide the amount of people asked before a birthday is duplicate
by the number of trials to obtain the average amount of trials to get 2
duplicate birthdays
'''














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
    
    

        
