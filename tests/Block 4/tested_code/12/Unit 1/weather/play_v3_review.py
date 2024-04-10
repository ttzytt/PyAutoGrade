



Want = str(input("Do you want to play outside?"))


if Want=="No":
    print("You shouldn't play outside.")
else:



    Fahrenheit = float(input("What is the temperature today(in °F)?"))
    if Fahrenheit > 95 or Fahrenheit <32:
        print("You shouldn't play outside today.")
    elif Fahrenheit>=32 and Fahrenheit<=50:
            Jacket = input("Do you have a jacket?")
            if Jacket == "Yes":
                print("You should play outside today.")
            if Jacket == "No":
                print("You shouldn't play outside today.")
    elif Fahrenheit>50 and Fahrenheit <=95 :
        Rain= input("Is it raining?")
        if Rain == "Yes":
            Jacket = input("Do you have a jacket?")
            if Jacket == "No":
                print("You shouldn't play outside today.")
            if Jacket == "Yes":
                print("You should play outside today.")
    else:
        print("You should play outside today.")


