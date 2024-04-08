


import random



def tries_until_duplicate_birthday(include_leap_year = False):
    
    birthdays = []
    birthday = random.randint(1,365)
    
    while birthday not in birthdays:
        
        birthdays.append(birthday)

        if include_leap_year:
            
            if random.randint(1,4) == 1:
                birthday = random.randint(1, 366)
            else:
                birthday = random.randint(1,365)
        
        else:
            birthday = random.randint(1, 365)
                

    
    return len(birthdays)



def average_until_duplicate_birthday(num_trial, include_leap_year = False):
    sum = 0
    for i in range(num_trial):
        sum += tries_until_duplicate_birthday(include_leap_year)

    return sum/num_trial

while True:
    
    num_trial = input('How many trials do you want to run: ')

    print('Your average was ' + str(average_until_duplicate_birthday(int(num_trial), True)) + ' times.')






