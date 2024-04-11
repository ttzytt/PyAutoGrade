



cat_or_not = input("Are you a cat? (yes/no): ")


if cat_or_not.lower() == "yes":
    
    temp = int(input("What's the temperature in °F? "))

    

    
    if 40 <= temp <= 85:
        
        rain = input("Is it raining outside? (yes/no): ")
        
        
        if rain.lower() == "yes":
            
            print("Go sit on your master's keyboard while they are working.")
            
        else:
            print("Go outside and play. Bring a dead animal home as a gift.")

    
    elif temp > 85:
        
        print("Knock things off counters until anyone notices you, then lay on back and make cute noises.")

    
    elif temp < 40:
        
        print("Steal some food, take it to your owner's bed and eat it under the warm blanket.")



else:
    print("ERROR: Oops, sorry you have been blocked...")
