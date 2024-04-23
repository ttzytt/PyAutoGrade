



F = int(input("what the temperature today in °F?")) 



if F >= 90 or F < 50: 
    print("You shouldn't play outside today:(")
elif F <90 or F >=50:
    rain = input("Is it raining?")
    if rain =="no":
        print("You should play outside today:p!")
    elif rain == "yes":
        jacket = input("Do you wear a jacket?")
        if jacket == "yes":
            print("You should play outside today!")
        elif jacket == "no":
            print("You shouldn't play outside today:(")
   





