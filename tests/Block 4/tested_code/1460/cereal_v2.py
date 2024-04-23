



cereal_pieces = {'red': 6, 'blue': 5, 'yellow': 7, 'orange': 7, 'purple': 4, 'green': 6}

desired_cereal_pieces = input("Enter cereal pieces: ").lower()
while desired_cereal_pieces != 'quit':
    desired_banana_split = desired_cereal_pieces.split()
    if len(desired_banana_split) > 0 and desired_banana_split[0] == 'floor':
        for i in range(1,len(desired_banana_split)):
            cereal = desired_banana_split[i]
            if cereal in cereal_pieces:
                cereal_pieces[cereal] += 1
            else:
                cereal_pieces[cereal] = 1
            print("Added 1", cereal)
    else:
        cereal_sum = 0
        for cereal in desired_banana_split:
            if cereal not in cereal_pieces:
                print("Couldn't find", cereal,
                      "/ Will not be including it in the count.")
            else:
                cereal_sum += cereal_pieces[cereal]
        if cereal_sum == 1:
            print("There is a single fruit loop with those colors.")
        else:
            print("There are", cereal_sum, "fruit loops with those colors.")
    desired_cereal_pieces = input("Enter cereal pieces: ").lower()
print("""(Black screen with text; The sound of buzzing bees can be heard)
According to all known laws
of aviation,
 :
there is no way a bee
should be able to fly.
 :
Its wings are too small to get
its fat little body off the ground.
 :
The bee, of course, flies anyway
 :
because bees don't care
what humans think is impossible.
BARRY BENSON:
(Barry is picking out a shirt)
Yellow, black. Yellow, black.
Yellow, black. Yellow, black.
 :
Ooh, black and yellow!
Let's shake it up a little.
JANET BENSON:
Barry! Breakfast is ready!
BARRY:
Coming!
 :
Hang on a second.
(Barry uses his antenna like a phone)
 :
Hello?""")
