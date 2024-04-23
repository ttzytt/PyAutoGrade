



farenheit = int(input('What\'s the temparature in farenheit today? '))
if farenheit <= 32 or farenheit >= 95:
#Shouldn't play outside when temperature is too high or too low
 print('You shouldn\'t play outside today')
elif farenheit <= 50 and farenheit >= 32:
    jacket = input('Do you have a jacket?')
#In cold days, jacket is required regardless of rain
    if jacket == 'yes':
     print('You should play outside today')
    elif jacket == 'no':
     print('You shouldn\'t play outside today')
else:
    rain = input('Is today gonna rain?')
    if rain == 'yes':

     if jacket == 'yes':
      print('You should play outside today')
     elif jacket == 'no':
      print('You shouldn\'t play outside today')
    elif rain == 'no':
#If no rain and warm then jacket isn't required
     print('you should play outside today')
      
