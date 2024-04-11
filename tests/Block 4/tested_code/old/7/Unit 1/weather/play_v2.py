




temp_f = float(input('What is the temperature today (in °F)? '))
print()
if temp_f >= 95 or temp_f <= 32:
   print("You shouldn't play outside today.")

elif temp_f < 95 and temp_f >= 50:
    rain = input("Is it raining? ")
    print()
    if rain == ("yes" or "Yes"):
        jacket_1 = input("Do you have a jacket? ")
        print()
        if jacket_1 == ("yes" or "Yes"):
            print("You should play outside today.")
        else: print("You shouldn't play outside today.")
    else: print("You should play outside today.")    

elif temp_f > 32 and temp_f < 50:
    jacket_2 = input("Do you have a jacket? ")
    print()
    if jacket_2 == ("yes" or "Yes"):
        print("You should play outside today.")
    else: print("You shouldn't play outside today.")




