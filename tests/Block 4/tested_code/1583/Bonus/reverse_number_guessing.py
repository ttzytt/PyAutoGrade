



possible_numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]


start = input('''
Think of a number from 1 to 10.
I will try to ask questions and guess your number.
Ready? Press Enter ''')

print()

is_odd = input('Is your number odd? ')
if is_odd.lower() == 'yes': 
    
    possible_numbers.remove(2)
    possible_numbers.remove(4)
    possible_numbers.remove(6)
    possible_numbers.remove(8)
    possible_numbers.remove(10)
    is_divisible_by_3 = input('Is your number divisible by 3? ')
    if is_divisible_by_3.lower() == 'yes': 
        possible_numbers.remove(1)
        possible_numbers.remove(5)
        possible_numbers.remove(7)
        is_prime = input('Is your number prime? ')
        if is_prime.lower() == 'yes': 
            possible_numbers.remove(9)
        else: 
            possible_numbers.remove(3)
    else: 
        possible_numbers.remove(3)
        possible_numbers.remove(9)
        is_divisible_by_5 = input('Is your number divisible by 5? ')
        if is_divisible_by_5.lower() == 'yes': 
            possible_numbers.remove(1)
            possible_numbers.remove(7)
        else: 
            possible_numbers.remove(5)
            is_prime = input('Is your number prime? ')
            if is_prime.lower() == 'yes': 
                possible_numbers.remove(1)
            else: 
                possible_numbers.remove(7)
else: 
    possible_numbers.remove(1)
    possible_numbers.remove(3)
    possible_numbers.remove(5)
    possible_numbers.remove(7)
    possible_numbers.remove(9)
    is_less_than_7 = input('Is your number less than 7? ')
    if is_less_than_7.lower() == 'yes': 
        possible_numbers.remove(8)
        possible_numbers.remove(10)
        is_divisible_by_3 = input('Is your number divisible by 3? ')
        if is_divisible_by_3.lower() == 'yes': 
            possible_numbers.remove(2)
            possible_numbers.remove(4)
        else: 
            possible_numbers.remove(6)
            is_prime = input('Is your number prime? ')
            if is_prime.lower() == 'yes': 
                possible_numbers.remove(4)
            else: 
                possible_numbers.remove(2)
    else: 
        possible_numbers.remove(2)
        possible_numbers.remove(4)
        possible_numbers.remove(6)
        is_divisible_by_5 = input('Is your number divisible by 5? ')
        if is_divisible_by_5.lower() == 'yes': 
            possible_numbers.remove(8)
        else: 
            possible_numbers.remove(10)


print(possible_numbers[0])







        
