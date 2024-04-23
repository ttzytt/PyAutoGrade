



def comments_for_functions(in_file, out_file):
    with (open(in_file, 'r') as file_in,
            open(out_file, 'w') as file_out):
        list_of_lines = file_in.readlines()
        i = 0
        while i < len(list_of_lines):
            if len(list_of_lines[i]) >= 3 and i != 0:
                if list_of_lines[i][:3] == "def" and (list_of_lines[i-1][0] != '#'
                                                      and (list_of_lines[i-1][-4:] != "'''\n"
                                                           and list_of_lines[i-1][-4:] != '"""\n')):
                    list_of_lines.insert(i, '#R(auto): Add a comment that says what this function does!\n')
                    i += 1
            i += 1
        file_out.writelines(list_of_lines)

def blank_lines_around_functions(in_file, out_file):
    with (open(in_file, 'r') as file_in,
            open(out_file, 'w') as file_out):
        list_of_lines = file_in.readlines()
        
        i = 0
        while i < len(list_of_lines):
            if len(list_of_lines[i]) >= 3 and i != 0:
                if list_of_lines[i][:3] == "def":
                    for j in range(i-1, 0, -1):
                        if list_of_lines[j][0] != '#':
                            if list_of_lines[j][0] != '\n':
                                list_of_lines.insert(j+1, '\n')
                                i += 1
                            break
                        
                    for k in range(i+1, len(list_of_lines), 1):
                        if list_of_lines[k][0] == '\t' or list_of_lines[k][0] == ' ':
                            continue
                        elif list_of_lines[k][0] != '\n':
                            list_of_lines.insert(k, '\n')
                            i += 1
                            break
                        else:
                            break
            i += 1
            
        file_out.writelines(list_of_lines)


blank_lines_around_functions("just_for_test.py", "T-test.py")
                    
