



'''
Returns words to remind add comments if there isn't any comments in a function.
    inputs:
        out_file    A file that will print reminds in it.
        in_file    A file that you want to check.
'''

def comments_for_functions(in_file, out_file):
    #list_of_lines = in_file.readlines()
    list_of_words = in_file.readlines()
    #print(list_of_words)
    for i in range(len(list_of_words)):
        if 'def' in list_of_words[i] and '
            list_of_words[i] = comment + '\n' + list_of_words[i]
            
        out_file.writelines(list_of_words)

comment = '#R(auto): Add a comment that says what this function does!'
in_file = 'file_writing.py'
out_file = 'file_writing_auto_review.py'

with open(out_file, 'w') as out_file, open(in_file, 'r') as in_file:
    comments_for_functions(in_file, out_file)




'''
Returns words to remind add comments if there isn't any comments in a function.
    inputs:
        out_file    A file that will print reminds in it.
        in_file    A file that you want to check.
'''

def comments_for_functions_Bouns_1(in_file, out_file):
    #list_of_lines = in_file.readlines()
    list_of_words = in_file.readlines()
    #print(list_of_words)
    for i in range(len(list_of_words)):
        if 'def' in list_of_words[i]:
            if '
                list_of_words[i] = comment + '\n' + list_of_words[i]
                
            out_file.writelines(list_of_words)

comment = '#R(auto): Add a comment that says what this function does!'
in_file = 'file_writing.py'
out_file = 'file_writing_auto_review.py'

with open(out_file, 'w') as out_file, open(in_file, 'r') as in_file:
    comments_for_functions(in_file, out_file)





'''
Returns a blank line if there isn't any blanks before comments.
    inputs:
        out_file    A file that will print reminds in it.
        in_file    A file that you want to check.
'''
def blank_lines_around_functions(in_file, out_file):
    blank = '\n'
    list_of_words = in_file.readlines()
    print(list_of_words)
    for i in range(len(list_of_words)):
        if '
            list_of_words[i] = blank + '\n' + list_of_words[i]
        
    out_file.writelines(list_of_words)
        

in_file = 'test.py'
out_file = 'test_2.py'

with open(out_file, 'w') as out_file, open(in_file, 'r') as in_file:
    blank_lines_around_functions(in_file, out_file)



