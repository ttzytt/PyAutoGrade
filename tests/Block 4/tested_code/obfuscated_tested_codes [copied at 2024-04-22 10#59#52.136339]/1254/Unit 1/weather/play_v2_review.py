

 
temperature = int(input('What is the temperature today (in °F)? '))

if temperature > 95 and temperature < 32:
    print("You shouldn't play outside today.")

if temperature <= 95 and temperature >= 32:
    raining = input('Is it raining? ')
    if raining == 'yes':
        jacket = input('Do you have a jacket? ')
        if jacket == 'yes':
            print('You should play outside today.')
        if jacket == 'no':
            print("You shouldn't play outside today.")
    elif raining == 'no':
        if temperature >= 50:
            print('You should play outside today.')
        else:
            jacket = input('Do you have a jacket? ')
            if jacket == 'yes':
                print('You should play outside today.')
            if jacket == 'no':
                print("You shouldn't play outside today.")
        
    
'''R
Missing some elifs in line 9, 15, 24.
There should be no unecessary questions.  For example, when the temperature is 40, it doesn't matter if it is
raining or not.  Therefore, you should not ask if it is raining.  It only matters if you have a jacket or not.
Asking if it is raining between 32 and 50 degrees is useless.
Splitting the 3 major cases apart can help the readability of the code.  You know exactly what the code is going to
do and when without the confusion of multiple cases in one block of code.
'''
