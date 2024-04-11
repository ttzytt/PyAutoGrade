




temperature_in_f = int(input('What is the temperature today (in °F)? '))  

if(temperature_in_f > 90):
    print('Wow that\'s hot') # If above 90 prints 'Wow that's hot'
elif(32 <= temperature_in_f < 50):
    print('That\'s so cold') # If above or equal to 32 or below 50 prints 'That's so cold'
elif(temperature_in_f < 32):
    print('That\'s freezing') #If less than 32 prints 'That's freezing'

temperature_in_c = 5/9 * (temperature_in_f-32) 

print('That\'s ' + str(temperature_in_c) + ' °C.') 
