






temperature_fahrenheit = int(input('What is the temperature today (in °F)? '))




if temperature_fahrenheit > 95 or temperature_fahrenheit < 32:
    
    print('You should not play outside today.')

elif 95 > temperature_fahrenheit > 50:
    
    rain_answer = input('Is it raining? ').lower()



    if rain_answer == 'yes':

        jacket_answer = input('Do you have a jacket? ').lower()

        if jacket_answer == 'yes':

            print('You can play outside today.')

        elif jacket_answer == 'no':

            print('You should not play outside today.')

    elif rain_answer == 'no':

        print('You can play outside today.')

else:

    jacket_answer = input('Do you have a jacket? ').lower()

    if jacket_answer == 'yes':

        print('You can play outside today.')

    elif jacket_answer == 'no':

        print('You should not play outside today.')















