






def comments_for_functions(in_file, out_file):
    
    list_of_lines = in_file.readlines()
    
    for i in range(len(list_of_lines)):
        
        if list_of_lines[i][:4] == 'def ' and list_of_lines[i-1][0] != '#':
                out_file.write('#R(auto): Add a comment that says what this function does!\n')
        out_file.write(list_of_lines[i])
        





def blank_lines_around_functions(in_file, out_file):
    list_of_lines = in_file.readlines()
    new_list_of_lines = []
    for i in range(len(list_of_lines)):
        if list_of_lines[i][:4] == 'def ':
            current_line = i - 1
            while list_of_lines[current_line][0] == '#':
                current_line -= 1
            if len(list_of_lines[current_line].split()) != 0:
                new_list_of_lines.insert(current_line, "\n")
        new_list_of_lines.append(list_of_lines[i])
        
    for i in range(len(new_list_of_lines)):
        out_file.write(new_list_of_lines[i])
            















in_file_name = 'Text files/auto_review_in_file.py'
out_file_name = 'Text files/auto_review_out_file.py'
with open(in_file_name, 'r') as in_file, open(out_file_name, 'w') as out_file:
    comments_for_functions(in_file, out_file)

in_file_name = 'Text files/blank_lines_in_file.py'
out_file_name = 'Text files/blank_lines_out_file.py'
with open(in_file_name, 'r') as in_file, open(out_file_name, 'w') as out_file:
    blank_lines_around_functions(in_file, out_file)
