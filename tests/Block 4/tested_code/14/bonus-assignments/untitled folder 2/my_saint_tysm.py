



Things_to_check = {
        'has_starting_comment': True,
        'is_reviewed': True,
        'no_review_comments': True,
        'comments_not_too_long': True,
        'code_not_too_long': True,
        'not_too_many_tabs': True,
    }

NAME = "Albert Zhao"
MAX_CHARACTERS =   100
CHARS_PER_TAB = 4
FILE_NAME = ""

def check_first_n_characters(target_text, actual_text, n = None):
    if len(target_text) > len(actual_text) or (n is not None and n > max(len(target_text), len(actual_text))):
        return False
    if n is None:
        n = len(target_text)
    for i in range(n):
        if actual_text[i] != target_text[i]:
            return False
    return True

def is_full_line_comment(line: str) -> bool:
    if len(line) == 0:
        return False
    return line.strip()[0] == "#"

def check(file_path):
    with open(file_path, 'r') as file:
        my_file_content = file.read()
     
    my_file_lines = my_file_content.split('\n')
    
    File_things_to_check = Things_to_check.copy()
    Fttc = File_things_to_check

    
    author_line = my_file_lines[0]
    if check_first_n_characters(f"# Written by: {NAME}", author_line):
        Fttc['has_starting_comment'] = True
    else:
        Fttc['has_starting_comment'] = False

    reviewer_line = my_file_lines[1]
    if check_first_n_characters(f"# Reviewed by: ", reviewer_line):
        Fttc['is_reviewed'] = True
    else:
        Fttc['is_reviewed'] = False

    
    if '#R' in my_file_content:
        Fttc['no_review_comments'] = False
    else:
        Fttc['no_review_comments'] = True

    
    Fttc['not_too_many_tabs'] = True
    Fttc['comments_not_too_long'] = True
    Fttc['code_not_too_long'] = True
    for line in my_file_lines:
        number_of_tabs = line.count("\t")
        if number_of_tabs > (MAX_CHARACTERS * 1/2 / CHARS_PER_TAB): 
                                                                    
            Fttc['not_too_many_tabs'] = False

        if len(line) > MAX_CHARACTERS:
            if len(line.strip()) > 0:
                if '#' in line:
                    if line.index('#') > int(MAX_CHARACTERS * 3/4): 
                        Fttc['code_not_too_long'] = False
                    else:
                        Fttc['comments_not_too_long'] = False
                else:
                    Fttc['code_not_too_long'] = False

    return Fttc

def change(file_path, Fttc):
    new_file_content = ""
    with open(file_path, 'r') as file:
        my_file_content = file.read()
    file_lines = my_file_content.splitlines()  
    lines_to_write = file_lines.copy()

    if Fttc['has_starting_comment'] is False:
        
        if not isinstance(NAME, str):
            raise(ValueError, "NAME not set.")

        if is_full_line_comment(file_lines[0]) and ("written by" in file_lines[0].lower() or "author:" in file_lines[0].lower()): 
            
            print("Replaced line '",lines_to_write.pop(0),"' with:", end=" ")
        else:
            print("Wrote:", end=" ")
        lines_to_write.insert(0,f"# Written by: {NAME}")
        print(f"# Written by: {NAME}")

    if Fttc['is_reviewed'] is False:
        
        reviewer_name = input("Reviewer Name ('NADA' to skip.): ")
        if reviewer_name != 'NADA':
            if is_full_line_comment(file_lines[1]) and ("reviewer" in file_lines[1] or "reviewed:" in file_lines[1]): 
                
                print("Replaced line '",lines_to_write.pop(0),"' with:", end=" ")
            else:
                print("Wrote:", end=" ")
            lines_to_write.insert(0,f"# Reviewd by: {reviewer_name}")
            print(f"# Reviewd by: {reviewer_name}")

    if Fttc['no_review_comments'] is False:
        for i, line in enumerate(lines_to_write):
            if "#R" in line:
                if input(f'Delete "{lines_to_write[i][line.index("#R"):]}"? (ENTER for yes) ') == '':
                    lines_to_write[i] = lines_to_write[i][:line.index("#R")]
    
    file_path_without_extension = file_path[:-3]
    with open(f'{file_path_without_extension}_CHANGED.py', 'w') as f:
        f.write('\n'.join(lines_to_write))
    
    return f'{file_path_without_extension}_CHANGED.py'
    
    

    
    


















    


