



from random import randint


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

num_of_trials = input("How many trials would you like to run: ")
print(average_until_duplicate_birthday(int(num_of_trials), True))









