



temperature = int(input("what's the temperature today in °F? : "))
c = temperature
c = round((c- 32)/9*5, 2)
result = "That's " + str (c) + " °C."

if temperature > 90 :
    print ("wow that's hot.")

    print (result)
elif temperature <= 90 :
    if temperature < 32 :
        print ("That's freezing.")
        print (result)
    elif 32 <= temperature < 50 :
        print("That's so cold.")
        print (result)
    else :
        print (result)

        
