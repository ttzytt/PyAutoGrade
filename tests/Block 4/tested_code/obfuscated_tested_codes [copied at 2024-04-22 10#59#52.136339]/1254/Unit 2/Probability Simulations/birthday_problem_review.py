


import random

random.seed()



def tries_until_duplicate_birthday():
    list_of_birthdays = []
    birthday = [random.randint(1, 365)]
                                        
    while birthday not in list_of_birthdays:
        list_of_birthdays.append(birthday)
        birthday = [random.randint(1, 365)]
    return len(list_of_birthdays)





def average_until_duplicate_birthday(num_trials):
    sum_of_tries = 0
    for _ in range(num_trials):
        sum_of_tries += tries_until_duplicate_birthday()

    return (sum_of_tries/ num_trials)


num_trials = int(input('How many trials do you want? '))
print(average_until_duplicate_birthday(num_trials))





'''R
You need comments in the function.
put the average in a sentence.
'''
    


        
        
