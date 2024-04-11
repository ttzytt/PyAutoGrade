



farenheit = int(input('What\'s the farenheit temparature today? '))
if farenheit >= 90:
# Extra prompt if it's too hot
 print('Wow that\'s hot')
celsius = (farenheit-32)*5/9
# Transfer farenheit into celsius system
print('Today\'s temparature in celsius is ' + str(celsius) +'°C')
