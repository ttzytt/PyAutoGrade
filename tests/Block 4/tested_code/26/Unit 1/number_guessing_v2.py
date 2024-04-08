



import random
random.seed ()

target_number = random.randint(100,999)


print("The number is from 100 to 999")
print()
print("Here is some hints:")



def prime(n):
    count = 2
    
    while count <= n/2:
        if n % count == 0:
            return None
            break
        else:
            count = count + 1
            return 0


def factor_number(n):
    result = 0
    count = 1
    while count <= n:
        if n % count == 0: 
            result = result + 1
        count = count + 1
    return result



def sum_of_digits(n):
    hundred_digit = (n - (n % 100)) / 100
    unit_digit = n % 10
    ten_digit = (n  - (hundred_digit * 100 + unit_digit))/10
    return hundred_digit + ten_digit + unit_digit


def product_factor(n):
    result = 1
    count = 1
    while count <= n:
        if n % count == 0:
            result = result * count
        count = count + 1
    return result


if prime(target_number) is not None:
    print('The number is a prime')
else:
    print('The number is not a prime')
    
print("This number contains " + str(factor_number(target_number)) + ' factors')
print("The sum of digits is " + str(round(sum_of_digits(target_number))))
if factor_number(target_number) >= 8:
    print("The Product of factors is " + str(product_factor(target_number)))
print()


count = 1 
human = 10000 
print("You have five chances")
while count <= 5 and human != target_number:
    print()
    
    human = int(input('type a integer to guess the number: ')) 
    print()
    
    if human > target_number:
        print('Your number is larger than the answer')
    elif human < target_number:
        print('Your number is smaller than the answer')
    else:
        print('You are correct')
    count = count + 1
    
