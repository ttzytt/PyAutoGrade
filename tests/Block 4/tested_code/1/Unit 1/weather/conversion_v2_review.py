





F = int(input("What's the weather today (in F°)?"))

C =round((F - 32)*(5/9),2)



if F >= 95:
          print("wow that's hot!")
elif F <=30:
        print("That's freezing!")


print("That's " + str(C) + " C°.")


