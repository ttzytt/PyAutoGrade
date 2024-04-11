


temperature = int(input('what temperature is it today (in °F)? '))
conversion = str(round((temperature - 32)*(5/9),2)) 


if temperature >= 90:
        
        print('Wow thats hot.')
        print('Thats ' + conversion + '°C')

elif temperature > 32:
        
        print('Thats a normal temperature.')
        print('Thats ' + conversion + '°C')
        

else:
        
        print('Wow thats freezing.')
        print('Thats ' + conversion + '°C')
