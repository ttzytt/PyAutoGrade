




'''
This function
'''
def comments_for_functions(in_file, out_file):

    comment = '#R(auto): Add a comment that says what this function does!'
    i = 0
    
    list_of_lines = in_file.readlines() 
    while i < len(list_of_lines):
        if list_of_lines[i][:4] == 'def ':
            if list_of_lines[i - 1][0] != '#':
                list_of_lines.insert(i, comment)
                i += 2
            else:
                i += 1
                
    out_file.writelines(list_of_lines)
                    
                    
            


def main():

    
    in_file_name = 'Unit 1/ List functions/ list_functions.py'
    out_file_name = 'Text files/ testingt15.txt'
    with (open(in_file_name, 'r') as in_file, open(out_file_name, 'w') as out_file):
        comments_for_functions(in_file, out_file)
