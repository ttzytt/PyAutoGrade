




import random

def tries_until_duplicate_birthday():
    
    
    birthdays = []

    
    duplicate_found = False

    while not duplicate_found:
        
        birthday = random.randint(1, 365)

        
        if birthday in birthdays:
            
            duplicate_found = True
        else:
            
            birthdays.append(birthday)

    
    return birthdays



def average_until_duplicate_birthday(num_trials):
    total_tries = 0

    
    for _ in range(num_trials):
        
        birthdays = []  
        duplicate_found = False

        
        while not duplicate_found:
            birthday = random.randint(1, 365)

            
            if birthday in birthdays:
                duplicate_found = True
            else:
                birthdays.append(birthday)
                

        total_tries += len(birthdays)
        

    
    average_tries = total_tries / num_trials
    return average_tries


def run_simulation():
    
    num_trials = int(input("Enter the number of trials: "))

    
    average = average_until_duplicate_birthday(num_trials)
    print(f"Average number of people asked before a birthday is repeated: {average}")








tries_until_duplicate_birthday()
average_until_duplicate_birthday(1000)
run_simulation()        
