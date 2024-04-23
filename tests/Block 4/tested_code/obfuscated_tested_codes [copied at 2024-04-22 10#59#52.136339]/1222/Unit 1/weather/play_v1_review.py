

temperature = int(input('What is the temperature today (in °F)?'))
conversion = str(round((temperature - 32)*(5/9),2))



if temperature > 95:
    print("You shouldn't play outside today.")

elif temperature <= 50:
    print("You shouldn't play outside today.")

elif temperature < 100:
    print("You should play outside today.")

elif temperature > 50:
    print("You should play outside today.")


