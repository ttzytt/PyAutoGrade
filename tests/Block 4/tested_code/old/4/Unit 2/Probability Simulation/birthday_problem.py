



import random
random.seed()



def tries_until_duplicate_birthday():
    birthday = random.randint(1,365) 
    birthdays = [] 
    birthdays.append(birthday)
    for birthday in birthdays:
        birthday = random.randint(1,365)
        
        if birthday not in birthdays:
            
            birthdays.append (birthday)
    
    return len(birthdays)+1



def average_until_duplicate_birthday(num_trials):
    list_ = []
    for times in range(num_trials):
        list_.append(tries_until_duplicate_birthday())
    sum_ = 0
    for index in range(len(list_)):
        sum_ += list_[index]
    return sum_/num_trials


user_input = int(input('print how many trails you want to do: '))

print(tries_until_duplicate_birthday())
print(average_until_duplicate_birthday(user_input))
print()







