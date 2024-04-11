




import random

def tries_until_duplicate_birthday(include_leap_year=False):
    days_in_year = 366 if include_leap_year else 365
    birthday_list = []
    while True:
        
        birthday = random.randint(1, days_in_year)

        
        if birthday in birthday_list:
            return len(birthday_list) + 1  
        else:
            birthday_list.append(birthday)

def average_until_duplicate_birthday(num_trials, include_leap_year=False):
    total_people = 0
    for i in range(num_trials):
        total_people += tries_until_duplicate_birthday(include_leap_year)
    return total_people / num_trials

if __name__ == "__main__":
    
    num_trials = int(input("Enter the number of trials: "))
    result = average_until_duplicate_birthday(num_trials)

    print("Average number of people asked before a birthday is repeated:", result)

    
    known_solution = 24.6
    print("Difference from the known solution (24.6):", result - known_solution)

    
    num_trials_leap_year = int(input("Enter the number of trials for leap year version: "))
    result_leap_year = average_until_duplicate_birthday(num_trials_leap_year, include_leap_year=True)
    print("Average number of people asked before a birthday is repeated (including leap year):", result_leap_year)
