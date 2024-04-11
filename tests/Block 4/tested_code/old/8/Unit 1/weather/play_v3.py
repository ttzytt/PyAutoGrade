




want = input("Do you want to play outside? ")


if want == No:
    
    print("You shouldn't play outside.")
else:
    
    fahrenheit = float(input("What is the temperature today(in °F) ?"))

    if fahrenheit > 95 or fahrenheit <32:
        print("You shouldn't play outside today.")

    elif fahrenheit>=32 and fahrenheit<=50:
            jacket = input("Do you have a jacket? ")
            if jacket == "Yes":
                print("You should play outside today.")
            if jacket == "No":
                print("You shouldn't play outside today.")

    elif fahrenheit>50 and fahrenheit <=95 :
        rain= input("Is it raining? ")
        if rain == "Yes":
            jacket = input("Do you have a jacket? ")
            if jacket == "No":
                print("You shouldn't play outside today.")
            if jacket == "Yes":
                print("You should play outside today.")
    else:
        print("You should play outside today.")
