

temperature = int(input('What is the temperature today (in °F)? '))


if(temperature>95):
    print("You shouldn’t play outside today.")
if(temperature<32):
    print("You shouldn't play outside today.")
   
if(temperature>=32):
    if(temperature<=50):
        jacket = input("Do you have a jacket? " )
        if(jacket == "Yes"):
            print("You should play outside today.")
        else:
            print("You shouldn’t play outside today.")   

if(temperature>50):
    if(temperature<=95):
        raincheck = input("Is it raining? ")
        if(raincheck == "Yes"):
            jacket = input("Do you have a jacket? " )
            if(jacket == "Yes"):
                print("You should play outside today.")
            else:
                print("You shouldn’t play outside today.")
        if(raincheck == "No"):
            print("You should play outside today.")



        

