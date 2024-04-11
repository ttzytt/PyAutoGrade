


def comments_for_functions(in_file, out_file):
    with (open(in_file, 'r') as file_in,
            open(out_file, 'w') as file_out):
        list_of_lines = file_in.readlines()
        i = 0
        while i < len(list_of_lines):
            if len(list_of_lines[i]) >= 3 and i != 0:
                if list_of_lines[i][:3] == "def" and (list_of_lines[i-1][0] != '#' and list_of_lines[i-1][:3] != "'''"):
                    list_of_lines.insert(i, '#R(auto): Add a comment that says what this function does!\n')
                    i += 1
            i += 1
        file_out.writelines(list_of_lines)


comments_for_functions("just_for_test.py", "T-test.py")
                    
