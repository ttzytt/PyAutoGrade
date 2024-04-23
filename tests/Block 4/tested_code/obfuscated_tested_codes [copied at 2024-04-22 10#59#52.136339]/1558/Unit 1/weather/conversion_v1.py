


"""
This program lets the user input a temperature in farenheit and
Converts it to celcius.
Prompts the user to input a temperature in farenheit
"""

Farenheit = int(input('What is the temperature today ( In °F)? ' ))

Celsius= str((Farenheit - 32) / 1.8)

if Farenheit >= 90:
              print('Wow, that is hot')
              
              print('That is ' + Celsius + ' °C')
else:
              print('That is ' + Celsius + ' °C.')
              
