



temp_in_F = int(input('What is the temperature today (in °F)? ')) 


if (True != ( 50 < temp_in_F < 95 )):
    print('You shouldn\'t play outside today.') # If the temperature is not inbetween 50 and 95 then prints 'You shouldn’t play outside today.'
else:
    print('You should play outside today.')
