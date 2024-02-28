





farenheit = int(input(' What is the temperature today (in °F)? '))


celsius = (farenheit - 32) * 5/9





if farenheit >= 90:
    print (' Wow that is hot. ')
elif farenheit < 32:
    print (' That is freezing. ')
elif farenheit >= 32 and farenheit < 50:
    print (' That is so cold ')


print (f'That is {celsius:.2f} °C. ')
