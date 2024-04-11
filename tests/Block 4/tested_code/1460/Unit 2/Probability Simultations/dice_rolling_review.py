






from random import randint
from time import time 

def get_millis_time():
    return int(time() * 1000)


def tries_until_all_rolled_values():
    rolled_values = []
    tries = 0
    while len(rolled_values) < 6: 
        rolled_value = randint(1,6) 
        if rolled_value not in rolled_values: 
            rolled_values.append(rolled_value)
        tries += 1
    return tries 
            




def average_until_all_rolled_values(num_trials):
    sum_so_far = 0
    for _ in range(num_trials):
        sum_so_far += tries_until_all_rolled_values()
    return sum_so_far/num_trials

while True:
    num_of_trials = input("How many trials would you like to run: ")
    start_time = get_millis_time()
    average_number = average_until_all_rolled_values(int(num_of_trials))
    end_time = get_millis_time()
    
    print(f'Average Number of Tries: {average_number:<.4} ||| Time Taken: {end_time-start_time} ms')
