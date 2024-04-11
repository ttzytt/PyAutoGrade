



def comments_for_functions(in_file, out_file):
    in_file_contents = in_file.readlines()
    print(in_file_contents)
    line_index = 0
    while line_index < len(in_file_contents):
        line = in_file_contents[line_index].strip()
        if 'def ' in line:
            prev_line = in_file_contents[line_index-1].strip()
            if not ('#' in prev_line or "'''" in prev_line or '"""' in prev_line):
                in_file_contents.insert(line_index,
                                        '#R(auto): Add a comment that says '
                                        + 'what this function does!\n')
                line_index += 1

        line_index += 1

    out_file.writelines(in_file_contents)

with (open('Text files/get_auto_reviewed.py', 'r') as in_file,
      open('Text files/get_auto_reviewed_review.py', 'w') as out_file):
    comments_for_functions(in_file, out_file)
