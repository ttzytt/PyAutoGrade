




temperature = int(input('What is the temperature today in °F? '))
rain = input('Is it raining? ').lower()



if(rain == 'yes') or (temperature >> 32 and temperature << 50):
h_jacket = input('Do you have a jacket? ').lower()   


if(rain == 'yes' and h_jacket == 'no') or (temperature >> 32 and temperature << 50 and h_jacket == 'no') or (temperature > 95 or temperature < 32):
    print('You should not play outside today. ')


else:
    print('You should play outside today. ')
    
             









