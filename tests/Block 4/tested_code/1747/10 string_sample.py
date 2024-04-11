def print_blank_lines():
    print('\n' * 4)






phrase = 'Sleep with the fishes'
print(phrase[4])  
print(phrase[6:10])  
                     
print(phrase[9:5:-1])  
print(phrase[:4] + phrase[-4:])  
                                 
print('The string has length ' + str(len(phrase)))
print_blank_lines()

"""
Remember that strings are immutable, so statements like
    phrase[1] = 'h'
will not work. Though we could accomplish something similar
using
    phrase = phrase[0] + 'h' + phrase[2:]
"""





response = 'qUiT'  
print(response.lower())  
                         
print(response)  
response = response.lower()  
print(response)  
print_blank_lines()

"""
Tip: If you never want to store the non-lowercased version, you can convert
before storing. For example,
    response = input('Enter your response: ').lower()
"""





"""
The end of a line is denote by the special character '\n'.

Notes:
• That's a backslash, not a slash. On Mac, it's between 'return' and 'delete'
  (on PC, between 'enter' and 'backspace').
• Yes, it looks like two characters, but it counts as one.

Some special characters in Python are represented by a backslash (\)
followed by another character. Here are some examples:
    \n    new line character
    \t    tab character  (indents text, though note that in IDLE, hitting
                          the tab key inserts 4 spaces, not a tab character)
    \\    backslash character  (a single \ means the start of a special
                                character, so we need \\ for a regular \)
    \'    single quote  (this can be used to insert the ' in the string
                         'I said "No, it isn\'t!"')
    \"    double quote  (this can be used to insert the "s in the string
                         "I said \"No, it isn't!\"")

Tip: If something isn't working right, make sure you are using \ and not /.
"""


## These count as one character, even though they look like 2. For example:
print(len('\t\ttest\n'))  ## 7 characters, not 10
print_blank_lines()



## We can store multiple lines of text in one string. Here is one way:
multiline_string_attempt = 'Here\nare\nmultiple\nlines\nof\text'
## It can be hard to read, though! Is the output what you expect?
print(multiline_string_attempt)
print_blank_lines()


# ------------------------  split, splitlines functions   ------------------------

sentence = 'This is so good\nof a sentence, yay!'
print(sentence)
## This splits a string into a list of 'words' (really, it splits when
## it sees characters like spaces and end-of-line characters).
words = sentence.split()
## Notice that punctuation became part of the words. We'll call that
## good enough!
print(words)
"""
Tip: You can then loop through the words using
    for word in words:
        ...
"""
print_blank_lines()




multiple_line_string = 'So\nmany\nlines of\ntext. Yay!'

lines = multiple_line_string.splitlines()  
                                           
print(lines[0])
print(lines[-1])
print_blank_lines()







pets = ['cat', 'dog', 'turtle']
pets_as_string_1 = ''.join(pets)  
pets_as_string_2 = ' '.join(pets)  
pets_as_string_3 = ' > '.join(pets)  
pets_as_string_4 = '\n'.join(pets)  

print(pets_as_string_1)
print(pets_as_string_2)
print(pets_as_string_3)
print(pets_as_string_4)
print_blank_lines()



lines = ['Here',
         'are',
         'multiple',
         'lines',
         'of',
         'text']
multiline_string = '\n'.join(lines)
print(multiline_string)
print_blank_lines()
