def comments_for_functions(in_file,out_file):
    lines = []
    for line in in_file:
        lines.append(line)
    for i in range(len(lines)):
        if lines[i][0] == 'd' and lines[i][1] == 'e' and lines[i][2] == 'f' and lines[i][3] == ' ' and lines[i-1][0] != '#':
            out_file.write('#R(auto): Add a comment that says what this function does!')
            out_file.write("\n")
            out_file.write(lines[i])
            out_file.write("\n")
        else:
            out_file.write(lines[i])
with (open('Text files/T15_read.py', 'r') as in_file,
        open('Text files/T15_write.py', 'w') as out_file):
    Task_15 = comments_for_functions(in_file, out_file)


def blank_lines_around_functions(in_file, out_file):
    true_func = 0
    lines = []
    for line in in_file:
        lines.append(line)
    for i in range (len(lines)-1):
        if lines[i][0] == 'd' and lines[i][1] == 'e' and lines[i][2] == 'f' and lines[i][3] == ' ' and lines[i-1][0] != "\n":
            true_func = 1
            out_file.write("\n")
            
        if lines[i][0] == ' ' and lines[i+1][0] != ' ' and lines[i+1][0] != "\n":
            if true_func == 1:
                out_file.write("\n")
            true_func = 0
            
            
        else:
            out_file.write(lines[i])
            a = 1


def break_up_long_lines(in_file, out_file):
    true_func = 0
    lines = []
    for line in in_file:
        lines.append(line)
    for i in range (len(lines)):
        if len(lines[i])>2:
            if lines[i][-2:] == "\n":
                if len(lines[i])>82:
                    out_file.write('#R(auto): Add a comment that says what this function does!')
                    out_file.write("\n")
                    out_file.write(lines[i])
                else:
                    out_file.write(lines[i])
            else:
                if len(lines[i])>80:
                    out_file.write('#R(auto): Add a comment that says what this function does!')
                    out_file.write("\n")
                    out_file.write(lines[i])
                else:
                    out_file.write(lines[i])
        else:
            out_file.write(lines[i])


def spaces_after_commas(in_file, out_file):
    true_func = 0
    lines = []
    for line in in_file:
        lines.append(line)
    for i in range (len(lines)):
        for j in range(len(lines[i])):
            if lines[i][j] == ',' and lines[i][j+1] != ' ':
                
                
                
			


with (open('Text files/T15_read.py', 'r') as in_file,
        open('Text files/T15_write.py', 'w') as out_file):
    Task_15 = 1
    

with (open('Text files/T16_read.py', 'r') as in_file,
        open('Text files/T16_write.py', 'w') as out_file):
    Task_16 = 1
    
    
with (open('Text files/T17_read.py', 'r') as in_file,
        open('Text files/T17_write.py', 'w') as out_file):
    Task_17 = break_up_long_lines(in_file, out_file)

with (open('Text files/T18_read.py', 'r') as in_file,
        open('Text files/T18_write.py', 'w') as out_file):
    Task_18 = spaces_after_commas(in_file, out_file)
