



"""
Teacher comments:
• Most important: Your reviewer gave helpful advice, and you
ignored it. This will always lose you points. And more importantly,
you are missing the opportunity to learn from your mistakes and
from your classmates.
• Most variable names, are ok, but pluralnoun needs to be
plural_noun.
• Needs comments!!!
• Comments (even the ones above) must start with spaces.
• The output needs spaces in many places

If I make comments in your code,
I will use ### to make them stand out.

Do not remove any of my comments.
"""
'''
### The prompts below needs a space after the :, or it's hard for the user

adjective = input('adjective:')
noun = input('noun:')
verb = input('verb in present tense:')
adverb = input('adverb:')
pluralnoun = input('plural noun:')  
color = input('color:')
animal = input('animal:')
number = input('number:')


print('Once upon a time in a ' \  
         + adjective + 'kindom, there lived a' + noun \
          + ' the '+ color + animal + '. ' + noun +\
          'was known throughout the land for' \
          + verb + number +pluralnoun + \
          'in one sitting, and the townsfolk were always amazed by how'\
          + adverb + noun + \
          'could do it. People came from far and wide to watch'\
          + noun + 's incredible feats of eating. It was a sight to behold')
          '''

# Prompts for user input, ensuring spaces after colons.
adjective = input('adjective: ')

noun = input('noun: ')

verb = input('verb in present tense: ')

adverb = input('adverb: ')

plural_noun = input('plural_noun: ')# Changed variable name to 'plural_noun'.

color = input('color: ')

animal = input('animal: ')

number = input('number: ')

# Generate and print the story with appropriate spaces.
print('Once upon a time in a ' +
      adjective + ' kingdom, there lived a ' + noun +
      ' the ' + color + ' ' + animal + '. ' + noun +
      ' was known throughout the land for ' + verb + ' ' + number +
      ' ' + plural_noun + ' in one sitting, and the townsfolk were always amazed by how ' +
      adverb + ' ' + noun + ' could do it. People came from far and wide to watch ' +
      noun + "'s incredible feats of eating. It was a sight to behold.")









