



temperature_in_f = int(input('What is the temperature today (in °F)? ')) 

if(temperature_in_f > 90):
    print('Wow that\'s hot') # If above 90 prints 'Wow that's hot'

temperature_in_c = 5/9 * (temperature_in_f-32) 

print('That\'s ' + str(temperature_in_c) + ' °C.') 
