

temperature = int(input('what temperature is it today (in °F)? '))


conversion = str(round((temperature - 32)*(5/9),2))
if temperature > 90:
        print( 'Wow thats hot.')
        print('Thats ' + conversion + '°C')



elif temperature < 90:
        print('Thats ' + conversion + '°C')
