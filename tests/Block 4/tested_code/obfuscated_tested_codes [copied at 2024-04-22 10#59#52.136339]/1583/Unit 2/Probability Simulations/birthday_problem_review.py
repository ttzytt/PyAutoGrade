


import random


random.seed()



def tries_until_duplicate_birthday():
    people_asked = 0
    birthdays_answered = [] 
    
    birthday_answered = 0 

    while birthday_answered not in birthdays_answered: 
                                                       
        birthdays_answered.append(birthday_answered) 
        birthday_answered = random.randint(1, 365)
        
    return len(birthdays_answered)




def average_until_duplicate_birthday(num_trials):
    
    
    average = 0
    for i in range(num_trials):
        average += tries_until_duplicate_birthday() 
                                                    
    average /= num_trials

    return average




while True:
    
    get_trials = int(input('How many times do you want to run the simulation? '))
    
    print('The average of the results is ' +
          str(average_until_duplicate_birthday(get_trials)) + '.')






