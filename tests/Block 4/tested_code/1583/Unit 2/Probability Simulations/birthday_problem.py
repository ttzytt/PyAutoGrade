





import random

random.seed()



def tries_until_duplicate_birthday():
    people_asked = 0
    birthdays_answered = [] 
    current_birthday = 0 

    while current_birthday not in birthdays_answered: 
                                                       
        birthdays_answered.append(current_birthday) 
        current_birthday = random.randint(1, 365)
        
    return len(birthdays_answered)




def average_until_duplicate_birthday(num_trials):
    
    sum_so_far = 0
    for i in range(num_trials):
        sum_so_far += tries_until_duplicate_birthday() 
                                                    
    average = sum_so_far / num_trials

    return average



while True:
    
    get_trials = int(input('How many times do you want to run the simulation? '))
    
    print('The average of the results is ' +
          str(average_until_duplicate_birthday(get_trials)) + '.')






