


"""
Teacher comments:
• The program crashes! You made changes without testing them!!!
• Variable names do not follow proper style.
• Has comments, but they don't make sense
• Comments must start with spaces.
• Prompts need spaces after them.

If I make comments in your code,
I will use ### to make them stand out.

Do not remove any of my comments.
"""

noun_1 = input('give me a noun:')  
animal_1 = input('give me an animal:')
noun_2 = input('give me a second noun:')
noun_3 = input('give me a third noun:')
place_1 = input ('give me a place:')
noun_4 = input ('give me a fourth noun:')


madlib = ('Once upon a time, there was a '+ noun_1 +
          ' class. It’s mainly about teaching ' + animal_1 + ' to use '
          + noun_2 + ' and '+noun_3+ '. Student’s would have the class on '+
          place_1+ ', it’s a room with bunch of ' + noun_4)

print(madlib)


ask = input ('do you want to have a another one? Choose Yes or No :')
if (ask == 'Yes'):
    name_1 = input('give me a name:')
    noun_5 = input('give me a noun:')
    verb_1 = input('give me a verb:')
    noun_6 = input('give me a noun:')
    adj_1 = input('give me a adj:')
    animal_2 = input('give me an animal:')

    madlibtwo = ('The was a guy named '+ name_1 +', he has got his '
                 +noun_5+' stolen because he forget to '+verb_1+
                 ' when he put it in the shared '+noun_6+'. He is so '
                 +adj_1+' about it that he told '+animal_2+ ' about it.')
    print(madlibtwo)

input('rate this from 1-5: ')

    
