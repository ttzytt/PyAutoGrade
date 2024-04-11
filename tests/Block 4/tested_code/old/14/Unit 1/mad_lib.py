




# vars
### Maybe "Inputs". This is code, everything has variables.
### Also, no abbreviations unless it's an exception we've discussed.
pluralNoun1 = input("noun, plural 1: ")
adjective = input("adjective: ")
place1 = input("place 1: ")
place2 = input("place 2: ")
landscapeFeature = input("landscape feature: ")
number = input("number: ")
pluralNoun2 = input("noun, plural 2: ")
pluralNoun3 = input("noun, plural 3: ")
verb = input("verb: ")
store = input("store (i.e. mcdonalds): ")
adverb = input("adverb: ")

### with, not w/
# actual text w/ + operator
# parentheses allows multiple lines to be used w/o python's compiler going mad
### Above comment provides some notes on how the code works, but not what it does.
### This is one of two types of comments that your code should have. Your comments
### should also provide a brief outline of the program.
madlibs = (

### The following code should be indented (since it's part of the line above it),
### with no blank lines around it.
"A long long time ago, there existed a group of " + pluralNoun1 + ". " +
"These " + pluralNoun1 + " were rather " + adjective +
" and traveled from " + place1 + " to " + place2 + ". " +
"However, when they were crossing a " + landscapeFeature +
", a North Carolinian troll stopped them in their paths." +
"\"Fee Fi Fo Fum. If you wanna cross I\'ma need sum,\" it said. " +
"Give me " + number + " " + pluralNoun2 + " and a stack of " + pluralNoun3 + ". " +
"The " + pluralNoun1 + " then " + adverb + " hoverboared to the nearest " + store +
" and " + verb + " the cashier."

)


print(madlibs)







