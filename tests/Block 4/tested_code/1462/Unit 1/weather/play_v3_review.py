



temperature = int(input('What is the temperature today (in °F)? '))

agree = input('Does your MOM agree you to play outside? (Yes/No) ')

if agree == 'Yes':

    if temperature > 95 or temperature < 32:
        print("You shouldn't play outside today.")


    elif temperature >= 32 and temperature <= 50:
        jacket = input('Do you have a jacket? ')

        if jacket == 'Yes':
            print("You should play outside today.")
        else:
            print("You shouldn't play outside today.")


    elif temperature <= 95 and temperature > 50:
        rain = input('Is it raining? (Capitalize the first letter) ')

        if rain == 'Yes':
            jacket = input('Do you have a jacket? ')
            if jacket == 'Yes':
                print("You should play outside today.")
            else:
                print("You shouldn't play outside today.")

        else:
            print("You should play outside today.")

else:
    for i in range(27):
        print('*',end='')
        
    print()
    print('* How Dare You!!! BWAAAAA *')
    
    for i in range(27):
        print('*',end='')

       
            

