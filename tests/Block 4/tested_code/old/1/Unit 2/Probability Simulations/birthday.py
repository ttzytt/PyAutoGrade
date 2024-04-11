


import random
random.seed()


def include_leap_year():
    
    user_leap = int(input("enter 1 to include leap year and 0 to not"))
    return (user_leap == 1)




def tries_until_duplicate_birthday(include_leap_year):

    

    birthdays = []

    
    
    if include_leap_year == True:
        leap_year = random.randint(1,4) 
        birthday = random.randint(1,366 if leap_year == 1 else 365) 
            
        while birthday not in birthdays:
            birthdays.append(birthday)
            birthday = random.randint(1,366 if leap_year == 1 else 365)
    else:
        birthday = random.randint(1, 365)

        while birthday not in birthdays:
            birthdays.append(birthday)
            birthday = random.randint(1, 365)
        
    return len(birthdays)



def avg_tries_until_duplicate_birthday(num_trial, include_leap_year):

    
    
    birthdays = []

    
    for i in range(num_trial):
        birthdays.append(tries_until_duplicate_birthday(include_leap_year))
    sum_birthdays = sum(birthdays)
    avg_birthdays = round(sum_birthdays/len(birthdays),2)
    return avg_birthdays



include_leap_year()
num_trial = int(input("How many trials do you want to do?"))
print(avg_tries_until_duplicate_birthday(num_trial, include_leap_year))

  
