






interger = int(input('Pick a number from 1 - 99: '))


if interger >= 90 :
    print('Wow, you fit ' + ' perfectly! ')

elif interger >= 51 and interger < 87:

    answer1 = input('When is your birthday? (month) ')
    
    if answer1 == str('July') or ('October'):
        answer2 = input('Can you fly? ')
        if answer2 == str('No'):
                print("You'd better choose a number between 12 and 45.")
        else:
            print('Wow, you are sooo lucky!!!!')

    else:
        print('Nice try~')
    

elif interger > 12 and interger < 45:

    answer2 == input('Can you fly? ')

    if answer2 == str('Yes'):
        
        print("You'd better choose a number bettween 51 and 87")
        
    else:
        answer1 = input('When is your birthday? (month) ')
        if answer1 == str('June') or str('Feberary'):
            print("Wow, it's your lucky number! ")
        
        else:
            print("That's a good number! ")

    
else:
    print("That's cool! Why not try again? ")
