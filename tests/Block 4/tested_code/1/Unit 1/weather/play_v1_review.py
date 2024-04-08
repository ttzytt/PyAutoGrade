



F = int(input("What's the weather today (in F°)?")) 
C =round((F - 32)*(5/9),2) 

if F >= 90 or F <= 50: 
    print("You should not play outside today.")
elif F <90 and F > 50:
    print("You should play outside today!")
