


import random

random.seed()



def tries_until_duplicate_birthday():
    birthday = random.randint(1, 365)
    birthdays = []
    birthdays.append(birthday)
    for birthday in birthdays:
        birthday = random.randint(1, 365)
        if birthday not in birthdays:
            birthdays.append(birthday)
    return len(birthdays)



def average_until_duplicate_birthday(num_trials):
    sum_results = 0
    for i in range(num_trials):
        result = tries_until_duplicate_birthday()
        sum_results = sum_results + result
    return sum_results / num_trials

user_input = int(input('How many times would you like to run this function?: '))
print()    

print(tries_until_duplicate_birthday())
print()

print(average_until_duplicate_birthday(user_input))
print()


