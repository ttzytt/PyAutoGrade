



temperature = int(input("What is the temperature today (in °F)? "))


is_raining = input("Is it raining? ")


jacket_needed = False


if (is_raining == "yes" and temperature < 50) or (temperature >= 32 and temperature <= 50):
    
    jacket_needed = True


have_jacket = None


if jacket_needed:
    have_jacket = input("Do you have a jacket? ")


if (temperature >= 60 and not jacket_needed) or (temperature >= 60 and jacket_needed and have_jacket == "yes"):
    print("You should play outside today")
else:
    print("You shouldn't play outside today")
