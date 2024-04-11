




temperature = float(input('What is the temperature today(in °F)? '))



if (temperature > 90 ):
    print('Wow that is hot.')
elif( temperature < 32 ):
    print('That’s freezing.')
elif (temperature < 50):
    
    print('That’s so cold.')
else:
    print('That’s normal.')

print('That is '+ str((temperature - 32) * 5/9) + ' °C')




