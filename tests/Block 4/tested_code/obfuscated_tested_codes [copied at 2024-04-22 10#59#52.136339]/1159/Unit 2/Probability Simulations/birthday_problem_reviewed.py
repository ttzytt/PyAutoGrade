'''
Written by: Alex Zhu
I did not receive help from my classmates and/or online resources
Reviewed by: Ethan Che
'''
import random
random.seed()





def tries_until_duplicate_birthday():
    birthdays = []
    asked = random.randint(1,365)
    
    
    while asked not in birthdays: 
        birthdays.append(asked)
        asked = random.randint(1,365)
    
    
    
    return len(birthdays) + 1
    



def average_until_duplicate_birthday(num_trials):
    times_total = 0
    for run_time in range(num_trials):
        tries_until_duplicate_birthday()
        times_total += tries_until_duplicate_birthday() 
    return times_total/num_trials
    
    
    




num_trials = int(input('For how many times do you want it to run? '))
print(average_until_duplicate_birthday(num_trials))


                 
