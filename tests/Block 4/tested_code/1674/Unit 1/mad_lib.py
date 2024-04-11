


"""
Teacher comments:
• adjective1 must be adjective_1. Same with other variables
• Needs comments!!! (see below)
• Formatting is great – overall looks really clean. The only thing is that
some of the lines of code are still too long (usual advice is to not go
past column 80, I didn't expect you to know this cutoff yet).

If I make comments in your code,
I will use ### to make them stand out.

Do not remove any of my comments.
"""

adjective1 = input('Enter an adjective: ')
color1 = input('Enter a color: ')
color2 = input('Enter a color: ')
color3 = input('Enter a color: ')
type_of_furniture = input('Enter a type of furniture: ')
plural_animal = input('Enter a plural animal: ')
type_of_food = input('Enter a type of food: ')
adjective2 = input('Enter an adjective: ')
noun = input('Enter a noun: ')
verb = input('Enter an action verb: ')


story = ('There was once a school that most people would find to be ' + adjective1 + '. Lockers were both ' + color1
         + ' and ' + color2 + '. ' + 'The walls were painted to be a neon ' + color3 + '. Instead of desks, there were '
         + type_of_furniture + '! ' + 'Throughout the different classrooms, ' + plural_animal +
         ' were kept in glass tanks. These ' + plural_animal + ' would scare all the students. During lunch, ' +
         type_of_food + ' was served, and it always tasted ' + adjective2 + '. At the end of a day, a ' + noun +
         ' is rung, and all the students ' + verb + ' out of the school.')

print(story)


