




import random

def tries_until_duplicate_birthday():
    birthdays = []
    tries = 0

    while True:
        birthday = random.randint(1, 365)
        tries += 1

        if birthday in birthdays:
            break
        else:
            birthdays.append(birthday)

    return tries
    
def average_until_duplicate_birthday(num_trials):
    total_tries = 0

    for _ in range(num_trials):
        total_tries += tries_until_duplicate_birthday()

    average_tries = total_tries / num_trials
    return average_tries


num_trials = int(input("Enter the number of trials: "))


result = average_until_duplicate_birthday(num_trials)
print(result)


