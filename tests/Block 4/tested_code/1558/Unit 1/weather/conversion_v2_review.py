


"""
This program lets the user input a temperature in
farenheit and responds with the temperature in
celsius and comments on how hot or cold it is
"""


Farenheit = int(input('What is the temperature today ( In °F)? ' ))

Celsius = str((Farenheit - 32) / 1.8)


if Farenheit >= 90:
              print('Wow, that is hot')
              print('That is ' + Celsius + ' °C')
if Farenheit <= 32:
              print('Wow, that is freezing')
              print('That is ' + Celsius + ' °C')
if 32 < Farenheit <= 50:
              print('Wow, That is pretty cold')
              print('That is ' + Celsius + ' °C')

