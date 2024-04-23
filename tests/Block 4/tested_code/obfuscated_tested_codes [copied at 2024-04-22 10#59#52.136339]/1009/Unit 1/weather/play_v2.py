temperature = int(input("What's the temperature today in °F? : "))
raining = input ("Is it raining? : ")

if temperature > 95 or temperature < 50 :
    if 32 < temperature < 50 :
        if raining == "yes"or raining == "Yes":
            jacket = input ("Do you have a jacket? : ")
            if jacket == "yes"or jacket == "Yes":
                print ("You should play outside today.")
        elif raining == "no" or raining == "No":
            print ("You should play outside today.")
    else:
        print("You shouldn't play outside today.")
else :
    print ("You should play outside today.")
