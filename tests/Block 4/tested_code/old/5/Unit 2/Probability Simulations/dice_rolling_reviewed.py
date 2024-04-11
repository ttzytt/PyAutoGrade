






import random
random.seed()

def tries_until_six_values():
    numbers_rolled = []
    count = 0

    while len(numbers_rolled) < 6:
        
        random_number = random.randint(1, 6)
        
        if random_number not in numbers_rolled:
            numbers_rolled.append(random_number)
        
        count += 1
    return count

def average_for_six_unique_values(num_trials):
    total = 0
    
    for _ in range(1, num_trials):
        total += tries_until_six_values()
    
    return total/num_trials
        
num_trials = int(input('Enter how many trials you want to go through: '))
average_result = average_for_six_unique_values(num_trials)
print('The average amount of tries is ' + str(average_result))
