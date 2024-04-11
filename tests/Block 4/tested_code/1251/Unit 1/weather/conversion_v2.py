




temperature = float(input('What is the temperature today(in °F)? '))


print()


if temperature >= 90:
    print('Wow that is hot.')
elif 32 < temperature <= 50:
    print('That’s so cold.')
elif temperature <= 32:
    print('That’s freezing.')
else:
    print('That’s normal.')
    


temp = round(((temperature - 32) * 5/9), 2)


print('That is '+ str(temp) + ' °C')  

