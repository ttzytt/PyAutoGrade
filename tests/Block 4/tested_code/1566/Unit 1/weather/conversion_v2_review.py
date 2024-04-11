


temp = int(input('what temperature is it today (in °F)? '))
conv = str(round((temp - 32)*(5/9),2)) 
if temp > 90:
        print( 'Wow thats hot.')
        print('Thats' + ' ' + conv + ' °C')
if temp<32: 
        print('Thats freezing.')
if temp>=32 and temp<50:
        print('Thats so cold.')
elif temp <= 90:
        print('Thats' + ' ' + conv + ' °C')
   
