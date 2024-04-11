



'''
Returns words to remind add comments if there isn't any comments in a function.
    inputs:
        out_file    A file that will print reminds in it.
        in_file    A file that you want to check.
'''

def comments_for_functions(in_file, out_file):
    lines = in_file.strip()
    for i in lines:
        words = lines[i].split()
        words_2 = lines[i-1].split()
        if 'def' in words:
            if '
                lines[i-1].insert('#R(auto): Add a comment that says what this function does!', 0)

in_file = 'file_writing'
out_file = 'file_writing_auto_review'

with open(out_file, 'w') as my_file:
        my_file.write(comments_for_functions(in_file, out_file))
            
