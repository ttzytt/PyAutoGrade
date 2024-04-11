




temperature = int(input('What temperature is it today (in °F)? '))
conversion = str(round((temperature - 32) * (5/9), 2)) 
if temperature >= 90: 
        print('Wow thats hot.')
        print('Thats' + ' ' + conversion + ' °C.')
if temperature < 32:
        print('Thats freezing.')
if temperature >= 32 and temperature <= 50:
        print('Thats so cold.')
elif temperature < 90 and temperature > 50:
        print('Thats' + ' ' + conversion + ' °C.')

