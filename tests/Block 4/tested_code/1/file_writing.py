def write_diamond_pattern(out_file, width):
    """ 
    width = 3:
     x
    xxx
     x
    """
    cur_len = 1
    while cur_len <= width: 
        empty_spaces = (width - cur_len) // 2
        out_file.write(" " * empty_spaces)
        out_file.write("x" * cur_len)
        # change line 
        out_file.write("\n")
        cur_len += 2
    cur_len -= 4
    while cur_len > 0:
        empty_spaces = (width - cur_len) // 2
        out_file.write(" " * empty_spaces)
        out_file.write("x" * cur_len)
        # change line 
        out_file.write("\n")
        cur_len -= 2

def last_name_first(in_file, out_file):
    for line in in_file:
        # Remove any leading/trailing whitespace and split the line into first and last names
        first_name, last_name = line.strip().split()
        
        # Write the last name followed by a comma, then the first name to the output file
        out_file.write(f"{last_name}, {first_name}\n")
    in_file.seek(0); out_file.seek(0)

def add_and_write(in_file, out_file):

    for line in in_file:
        # Remove any leading/trailing whitespace and split the line into operands
        operand1, operand2 = line.strip().split('+')
        
        # Convert operands to integers and calculate the result
        result = int(operand1) + int(operand2)
        
        # Write the original problem followed by = and the result to the output file
        out_file.write(f"{operand1} + {operand2} = {result}\n")  

def blah_blah_blah(in_file_name, out_file_name):
    for line in in_file_name:
        # Remove any leading/trailing whitespace
        line = line.strip()
        
        # Check if the line length is greater than 20 characters
        if len(line) > 20:
            # Truncate the line to the first 15 characters and append ', blah blah blah'
            line = line[:15] + ', blah blah blah'
        
        # Write the modified or original line to the output file
        out_file_name.write(f"{line}\n")