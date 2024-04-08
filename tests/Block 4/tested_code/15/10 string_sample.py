def print_blank_lines():
    print('\n' * 4)






phrase = 'Sleep with the fishes'
print(phrase[4])  
print(phrase[6:10])  
                     
print(phrase[9:5:-1])  
print(phrase[:4] + phrase[-4:])  
                                 
print('The string has length ' + str(len(phrase)))
print_blank_lines()







response = 'qUiT'  
print(response.lower())  
                         
print(response)  
response = response.lower()  
print(response)  
print_blank_lines()










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
