




farenheit = int(input('What\'s the farenheit temperature today? '))
if farenheit >= 90:
 print('Wow that\'s hot')
elif farenheit <=50:
    if farenheit >=32:
     print('That\'s really cold')
    else:
     print('That\'s freezing')

else:
 print('The temperature is normal today')
celsius = (farenheit-32)*5/9
print('The celsius temperature today is ' + str(celsius) +'°C')

