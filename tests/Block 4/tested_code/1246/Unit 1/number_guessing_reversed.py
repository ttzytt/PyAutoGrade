




print('Think of a number between 1,10')

print("Enter 'y' for yes and 'no' for no")

odd_or_not = input('Is your number odd?: ')

if odd_or_not == 'y':
    greater_7 = input('Is your number greater than 7(not incl. 7): ')
    if greater_7 == 'y':
        print('Your number is 9')
    else:
        div_5 = input('Is your number divisible by 5: ')
        if div_5 == 'y':
            print('Your number is 5')
        else:
            div_3 = input('Is your number divisible by 3: ')
            if div_3 == 'y':
                print('Your number is 3')
            else:
                prime_or_not = input('Is your number prime or not: ')
                if prime_or_not == 'y':
                    print('Your number is 7')
                else:
                    print('Your number is 1')
else:
    prime_or_not = input('Is your number prime or not: ')
    if prime_or_not == 'y':
        print('Your number is 2')
    else:
        div_3 = input('Is your number divisible by 3: ')
        if div_3 == 'y':
            print('Your number is 6')
        else:
            div_5 = input('Is your number divisible by 5: ')
            if div_5 == 'y':
                print('Your number is 5')
            else:
                greater_7 = input('Is your number greater than 7: ')
                if greater_7 == 'y':
                    print('Your number is 8')
                else:
                    print('Your number is 4')
        

