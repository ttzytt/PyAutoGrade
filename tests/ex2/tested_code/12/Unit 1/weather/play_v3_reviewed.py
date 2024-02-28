



print('AQI refers to air quality index (typically from 0 to 500')
AQI = int(input('What\'s the air quality today?'))
#AQI = Air Quality Index
if AQI >= 300:
 print('You shouldn\'t go outside today')
elif AQI <= 100:
 print('Feel free to go outside today')
elif AQI >=100 and AQI <= 300:

 mask = input('Do you have a mask?')
 if mask == 'yes':
  print('Feel free to go outside today')
 elif mask == 'no':
  print('You shouldn\'t go outside today')
