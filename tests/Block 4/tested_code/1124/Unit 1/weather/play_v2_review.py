


tempF = float(input('What is the temperature today (in °F)? '))

if tempF >= 95 or tempF <= 32:
   print("You shouldn't play outside today.")

elif tempF < 95 and tempF >= 50:
    rain = input("Is it raining? ")
    if rain == ("yes" or "Yes"):
        jacket1 = input("Do you have a jacket? ")
        if jacket1 == ("yes" or "Yes"):
            print("You should play outside today.")
        else: print("You shouldn't play outside today.")
    else: print("You should play outside today.")    

elif tempF > 32 and tempF < 50:
    jacket2 = input("Do you have a jacket? ")
    if jacket2 == ("yes" or "Yes"):
        print("You should play outside today.")
    else: print("You shouldn't play outside today.")



"""
When making comments during the code you should put the comments under the specific
lines of code in the 'if' statements. Variable names should be lowercase with
underscores for a new word. Other then that, nice work :)!
The organization of the code looks great! :D

"""
