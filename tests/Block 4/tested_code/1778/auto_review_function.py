


def comments_for_functions(in_file, out_file):
    with (open(in_file, 'r') as in_file_name,
            open(out_file, 'w') as out_file_name):
        list_of_lines = in_file_name.readlines()
        for i in range(len(list_of_lines) - 1):
            if list_of_lines[i + 1][:3] == 'def' and list_of_lines[i][0] != '#':
                out_file_name.write('#R(auto): Add a comment that says what this function does')
            
            out_file_name.write(list_of_lines[i])
            
comments_for_functions('Text files/cool_file.txt', 'Text files/cool_file_reviewed.txt')
