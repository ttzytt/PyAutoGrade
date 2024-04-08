



temperature = int(input("what's the temperature today in °F? : "))
raining = input ("is it raining? : ")

if temperature > 95 or temperature < 50 :
    if 32 < temperature < 50 :
        if raining == "yes"or raining == "Yes":
            jacket = input ("do you have a jacket? : ")
            if jacket == "yes"or jacket == "Yes":
                print ("you should play outside today.")
        elif raining == "no" or raining == "No":
            print ("you should play outside today.")
    else:
        print("you shouldn't play outside today.")
else :
    print ("you should play outside today.")

