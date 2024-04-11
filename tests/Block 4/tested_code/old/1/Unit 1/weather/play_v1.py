




Fahrenheit = int(input("What's the weather today (in F°)? "))
Celsius =round((Fahrenheit - 32)*(5/9),2) 


if Fahrenheit >= 90 or Fahrenheit <= 50: 
    print("You should not play outside today.")
elif Fahrenheit <90 and Fahrenheit > 50:
    print("You should play outside today!")
