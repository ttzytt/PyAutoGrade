





tempature_fahrenheit = int(input("What is the tempature today (in °F)? "))




if tempature_fahrenheit > 95 or tempature_fahrenheit <= 32:
    print("You shouldn't play outside today.")
    
else:
    
    
    
    
    if tempature_fahrenheit > 50:
        jacket_needed = input("Is it raining? ")
    else:
        jacket_needed = "yes"

    
    if jacket_needed.lower() == "yes":
        
        jacket_response = input("Do you have a jacket? ")

        
        
        if jacket_response.lower() == "yes":
            print("You should play outside today.")
        else:
            print("You shouldn't play outside today.")

    
    else:
        print("You should play outside today.")


