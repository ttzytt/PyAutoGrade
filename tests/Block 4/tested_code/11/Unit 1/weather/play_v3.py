



weather = input("What's the weather like today? (Sunny/Cloudy/Rainy) ")

if weather == "sunny":
    
    sunscreen = input("Do you have sunscreen? (Yes/No) ")
    hat = input("Do you have a hat? (Yes/No) ")
    
    
    if sunscreen == "yes" and hat == "yes":
        print("It's a great day for a hike! Enjoy the sunshine.")
    else:
        print("You should go for a hike, but don't forget sunscreen and a hat!")
elif weather == "cloudy":
    
    water = input("Do you have a water bottle? (Yes/No) ")
    
    
    if water == "yes":
        print("It's a good day for a hike, even though it's cloudy. Stay hydrated!")
    else:
        print("You should go for a hike, but remember to bring a water bottle.")
elif weather == "rainy":
    
    umbrella = input("Do you have an umbrella? (Yes/No) ")
    
    
    if umbrella == "yes":
        print("You can still go for a hike, but be prepared for rain with an umbrella.")
    else:
        print("It's not a good day for a hike without an umbrella.")
else:
    
    print("I'm not sure about the weather conditions. Check a weather forecast and decide.")
