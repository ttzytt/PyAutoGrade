

temp = int(input('what temperature is it today (in °F)? '))
rain = input('Is it raining ')
if rain == ("yes"): 
    jacket = input('Do you have a jacket? ')
    if jacket == ("no"):
        print('You shouldnt go outside. ')
    else:
        print('You should go outide ')
if rain == ("no"):
    if temp <= 32 or temp >= 50:
        print('You shoulnt go outside ')
if rain == ("no" ): 
    if temp > 32 and temp < 50:
        if input('Do you have your jacket ') == ("no"):
            print('You shouldnt go outside ')
        else:
            print('You should go outside')
        
        







