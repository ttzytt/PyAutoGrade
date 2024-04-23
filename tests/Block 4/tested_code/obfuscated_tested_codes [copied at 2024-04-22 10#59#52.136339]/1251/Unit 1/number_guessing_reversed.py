




print("Please choose a number between 1 and 10 secretly")

print("Now, I'm going to ask you some questions, please enter 'y' for yes, 'n' for no")
print()




odd = str(input("Is your number odd? "))
if odd == 'y':
    prime = str(input("Is your number prime? "))
    if prime == 'y':
        divisible_3 = str(input("Is your number divisible by 3? "))
        if divisible_3 == 'y':
            print("3")
        else:
            divisible_5 = str(input("Is your number divisible by 5? "))
            if divisible_5 == 'y':
                print("5")
            else:
                print("7")
    else:
         divisible_3 = str(input("Is your number divisible by 3? "))
         if divisible_3 == 'y':
             print('9')
         else:
             print('1')
    
else:
    prime = str(input("Is your number prime? "))
    if prime == 'y':
        print('2')
    else:
        compare_to_7 = str(input("Is your numbr > 7? (7 doesn’t count) "))
        if compare_to_7 == 'y':
            divisible_5 = str(input("Is your number divisible by 5? "))
            if divisible_5 == 'y':
                print('10')
            else:
                print('8')
        else:
            divisible_3 = str(input("Is your number divisible by 3? "))
            if divisible_3 == 'y':
                print('6')
            else:
                print('4')
