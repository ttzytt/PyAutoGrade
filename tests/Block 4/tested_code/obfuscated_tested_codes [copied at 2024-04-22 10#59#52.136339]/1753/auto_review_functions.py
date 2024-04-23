








def comments_for_functions(in_file, out_file):
    list_of_lines = in_file.readlines()
    for i in range(len(list_of_lines)):
        if list_of_lines[i][:4] == 'def ':
            if list_of_lines[i - 1][0] != '#':
                list_of_lines.insert(i, '#R(auto): Add a comment that says what this function does!\n')
    out_file.writelines(list_of_lines)




def main():
    in_file_name = 'Text files/math_functions.py'
    out_file_name = 'Text files/math_functions_review.py'
    
    with (open(in_file_name, 'r') as in_file,
            open(out_file_name, 'w') as out_file):
        comments_for_functions(in_file, out_file)

        
if __name__ == "__main__":
    main()



                



