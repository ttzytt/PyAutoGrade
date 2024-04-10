


temperature = int(input('What temperature is it today (in °F)? ')) 
rain = input('Is it raining? ')

if rain == ("yes"): 
    jacket = input('Do you have a jacket? ')
    if jacket == ("no"):
        print('You shouldnt go outside. ')
    else:
        print('You should go outide ')
        
if rain == ("no"): 
    if temperature <= 32:
        print('You shouldnt go outside ')
if rain == ("no" ): 
    if temperature > 32 and temperature < 50:
        if input('Do you have your jacket? ') == ("no"):
            print('You shouldnt go outside ')
        else:
            print('You should go outside')
        
        







