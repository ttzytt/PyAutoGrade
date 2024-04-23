

'''
This code will let the user input a temperature,
and then tell them is they should play outside or not.
'''


tempF = float(input('What is the temperature today?(in Fahrenheit) '))
print()

if tempF > 95 or tempF < 50:
    print("You shouldn't play outside today.")

else:
    print("You should play outside today.")

