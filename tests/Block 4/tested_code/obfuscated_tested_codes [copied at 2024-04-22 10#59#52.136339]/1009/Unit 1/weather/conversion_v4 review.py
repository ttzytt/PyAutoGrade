



temperature = int(input("what's the temperature today in °F? : "))
c = temperature
c = ((c- 32)/9*5, 2)

result = "that's " + str (c) + " °C."


if temperature > 90 :
    print("wow that's hot.")
    
elif 32 <= temperature < 50:
    print("That's cold.")
    
elif temperature < 32 :
    print("That's freezing.")
    
else :
    print("That's normal.")

print(result)


    
