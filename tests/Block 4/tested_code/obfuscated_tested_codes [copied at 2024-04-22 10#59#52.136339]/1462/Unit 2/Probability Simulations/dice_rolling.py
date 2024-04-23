





"""
Summarization of my results:
When the num_trails is 10, the results varied from 12.2 to 17.1.
When the num_trails is 100, the results varied from 13.7 to 15.1.
When the num_trails is 1000, the results varied from 14.5 to 15.0.
When the num_trails is 10000, the results varied from 14.6 to 14.8.
The more trails there are, the accurate the results it is,
When it is 100000 or 1000000, it approaches to 14.7. It took a long
time to generate them because the tries are pretty big.
"""

import random
random.seed()



def tries_until_all_six():
    
    tries_value = []
    value = random.randint(1,6)
    count = 0

    
    while len(tries_value) != 6:
        if value not in tries_value:
            tries_value.append(value)
        value = random.randint(1,6)

        
        
        
        count = count + 1

    return count




def average_until_all_six(num_trails):
    sum_tries = 0

    for _ in range(num_trials):
        sum_tries = sum_tries + tries_until_all_six()

    return (sum_tries / num_trails)


num_trials = int(input('How many trails do you want to have? '))
print(average_until_all_six(num_trials))


    
        
