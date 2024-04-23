




"""
Checks if each function definition in the provided Python file has a preceding comment.
    If a comment is missing, a reminder comment is inserted above the function definition.
    
    Inputs:
        in_file: Path to the input file containing Python code (str).
        out_file: Path to the output file where the processed code will be saved (str).
    """
def comments_for_functions(in_file, out_file):
    lines = in_file.readlines()
    new_lines = []
    for i in range(len(lines)):
        line = lines[i]
        if line[:4] == 'def ':
            if i == 0 or not lines[i-1].strip()[:1] == '#': 
                new_lines.append('#R(auto): Add a comment that says what this function does!\n')
        new_lines.append(line)
    out_file.writelines(new_lines)



"""
    Modified version of comments_for_functions that also checks for docstring-style comments.
    
    Inputs:
        in_file: Path to the input file containing Python code (str).
        out_file: Path to the output file where the processed code will be saved (str).
    """
def comments_for_functions_b1(in_file, out_file):
    lines = in_file.readlines()
    new_lines = []
    for i in range(len(lines)):
        line = lines[i]
        if line[:4] == 'def ':
            previous_line = lines[i-1].strip() if i > 0 else ""
            if i == 0 or (not previous_line[:1] == '#' and not previous_line[-3:] in ("'''", '"""')):
                new_lines.append('#R(auto): Add a comment or docstring that says what this function does!\n')
        new_lines.append(line)
    out_file.writelines(new_lines)
  

"""
    Ensures there is a blank line before and after each function definition, for readability.
    
    Inputs:
        in_file: Path to the input file containing Python code (str).
        out_file: Path to the output file where the processed code will be saved (str).
    """
def blank_lines_around_functions(in_file, out_file):
    lines = in_file.readlines()
    new_lines = []
    for i in range(len(lines)):
        line = lines[i]
        if line[:4] == 'def ':
            if i > 0 and lines[i-1].strip() != '':
                new_lines.append('\n')
        new_lines.append(line)
        if i < len(lines) - 1:
            new_lines.append('\n')
    out_file.writelines(new_lines)

"""
    Adds a comment above any line exceeding 79 characters, suggesting it should be broken up.
    
    Inputs:
        in_file: Path to the input file containing Python code (str).
        out_file: Path to the output file where the processed code will be saved (str).
    """
def break_up_long_lines(in_file, out_file):
    lines = in_file.readlines()
    new_lines = []
    for line in lines:
        if len(line) > 79:
            new_lines.append('#R(auto): Line of code is too long. Break it up!\n')
        new_lines.append(line)
    out_file.writelines(new_lines)


 
"""
    Ensures there is a space after every comma in the code, unless followed by a newline.
    
    Inputs:
        in_file: Path to the input file containing Python code (str).
        out_file: Path to the output file where the processed code will be saved (str).
    """
def spaces_after_commas(in_file, out_file):
    lines = in_file.readlines()
    new_lines = []
    for line in lines:
        parts = [part.strip() for part in line.split(',')]
        corrected_line = ', '.join(parts)
        if line[-1] != '\n':
            corrected_line += '\n'
        new_lines.append(corrected_line)
    out_file.writelines(new_lines)


def main():
    
    with open('Text files/input_code.py', 'r') as in_file, open('Text files/output_comments_added.py', 'w') as out_file:
        comments_for_functions(in_file, out_file)

    
    with open('Text files/input_code.py', 'r') as in_file, open('Text files/output_comments_b1_added.py', 'w') as out_file:
        comments_for_functions_b1(in_file, out_file)

    
    with open('Text files/input_code.py', 'r') as in_file, open('Text files/output_blank_lines_added.py', 'w') as out_file:
        blank_lines_around_functions(in_file, out_file)

    
    with open('Text files/input_code.py', 'r') as in_file, open('Text files/output_long_lines_marked.py', 'w') as out_file:
        break_up_long_lines(in_file, out_file)

    
    with open('Text files/input_code.py', 'r') as in_file, open('Text files/output_spaces_after_commas_added.py', 'w') as out_file:
        spaces_after_commas(in_file, out_file)

if __name__ == "__main__":
    main()





