



cereal_pieces = {'red': 6, 'blue': 5, 'yellow': 7, 'orange': 7, 'purple': 4, 'green': 6}

desired_cereal_pieces = input("Enter cereal pieces: ").lower()
while desired_cereal_pieces != 'quit':
    cereal_sum = 0
    for cereal in desired_cereal_pieces.split():
        if cereal not in cereal_pieces:
            print("Couldn't find", cereal, "/ Will not be including it in the count.")
        else:
            cereal_sum += cereal_pieces[cereal]
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
