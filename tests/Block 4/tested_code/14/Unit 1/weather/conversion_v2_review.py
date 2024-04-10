

temp = int(input('What is the temperature today (in °F)? '))




if (temp > 90):
    print("Wow that's hot")
    print("That's " + str(round(((temp-32)*5/9),2)) + ' °C.')
elif (temp >55):
    print("That's normal")
    print("That's " + str(round(((temp-32)*5/9),2)) + ' °C.')   
elif (temp > 32):
    print("Wow that's cold")
    print("That's " + str(round(((temp-32)*5/9),2)) + ' °C.')

else:
    print("That's freezing")
    print("That's " + str(round(((temp-32)*5/9),2)) + ' °C.')


