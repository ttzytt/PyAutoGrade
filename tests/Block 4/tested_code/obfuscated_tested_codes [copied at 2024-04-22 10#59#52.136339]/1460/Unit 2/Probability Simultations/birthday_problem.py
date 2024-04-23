


from random import randint
from time import time 

def get_millis_time():
    return int(time() * 1000)


def tries_until_duplicate_birthday(include_leap_year = False):
    birthdays = []
    
    
    if include_leap_year:
        
        
        
        
        
        
        
        generated_birthday = randint(1 * 4,366 * 4) 
        generated_birthday = generated_birthday // 4
    else:
        generated_birthday = randint(1,365)
    
    while generated_birthday not in birthdays: 
                                               
        birthdays.append(generated_birthday) 
        if include_leap_year:               
            generated_birthday = randint(1 * 4,366 * 4)
            generated_birthday = generated_birthday // 4
        else:
            generated_birthday = randint(1,365)                                             

    
    return len(birthdays) + 1 
                              






def average_until_duplicate_birthday(num_trials, include_leap_year = False):
    sum_so_far = 0
    for _ in range(num_trials):
        sum_so_far += tries_until_duplicate_birthday(include_leap_year)
    return sum_so_far/num_trials

while True:
    
    num_of_trials = input("How many trials would you like to run: ")
    start_time = get_millis_time()
    average = average_until_duplicate_birthday(int(num_of_trials), False)
    end_time = get_millis_time()
    print("Trials:", average)
    print("Time:", end_time-start_time, "ms")



'''
test_values = [100, 1000, 10000]
for test_value in test_values:
    print(test_value, abs(average_until_duplicate_birthday(test_value) - 24.6))
'''

'''
100 - 2.1900000000000013 => 2.19 days
1000 - 0.402000000000001 => 0.402 days
10000 - 0.1343000000000032 => 0.1343 days
'''



