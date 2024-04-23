





import random
random.seed()


def tries_until_duplicate_birthday(include_leap_year = False): 
    birthdays = [] 
    i = 0
    if include_leap_year is True:
        while True:
            
            a = random.randint(0, 1460) 
            if a != 0:
                b = a%365
            else:
                b = 365 
                
            if not(b in birthdays):
                birthdays.append(b) 
                i += 1
                
                
            else:
                return i+1 
    else:
        while True:
            a = random.randint(1, 365) 
            if not(a in birthdays):
                birthdays.append(a) 
                i += 1
                
                
            else:
                return i+1 

def average_until_duplicate_birthday(num_trials, include_leap_year = False):
    f = 0 
    for _ in range(num_trials):
        f += tries_until_duplicate_birthday(include_leap_year)
    return f / num_trials * 1.00 

num_trial = input("How many trials do you want to have? ")
leap_year = input("Do you want to include leap years (Enter Yes or No)? ")


if leap_year == "Yes":
    include_leap_year = True
    
    j = average_until_duplicate_birthday(int(num_trial), include_leap_year)
    
else: 
    j = average_until_duplicate_birthday(int(num_trial))

print("The average amount of person we need to ask to find two with the same birthday is "
        + str(j))

"""
When I simulate using 100 trials, the average I get is 26.02 and 25.86
When I simulate using 1000 trials, the average I get is 24.67 and 27.494
This shows that the average will be more closed to the average across many trials
if the trial amount is larger.
"""
