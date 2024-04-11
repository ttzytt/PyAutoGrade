

type_1 = "'''"
type_2 = '"""'

def check_def(line):
    return (line[:4] == 'def ')
def check_comments (line):
    return ((line[0] == '#') or (line[:3] == type_1) or (line[:3] == type_2))
def check_blank(line):
    return (line == '\n')
def check_start(line): 
    return ((line[0] == ' ') and (line != '\n'))

def comments_for_functions(in_file, out_file):
    with(open(in_file,'r') as in_file, open(out_file,'w') as out_file):
        lines = in_file.readlines()
        if check_def(lines[0]):
            lines.insert(0,'#R(auto): Add a comment here that says what this function does!\n')
        for i in range(1,len(lines)):
            temp = lines[i]
            lines[i].remove(temp[:-1])
            if (check_def(lines[i]) and (not check_comments(lines[i-1]))):
                file.insert(i,'#R(auto): Add a comment here that says what this function does!\n')
        for i in range(len(lines)):
            out_file.write(lines[i])

def blank_lines_around_functions(in_file,out_file):
    with(open(in_file,'r') as in_file, open(out_file,'w') as out_file):
        lines = in_file.readlines()
        signal = 0
        if 'def' in lines[0]:
            lines.insert(0,'\n')
        for i in range(len(file)):
            if (check_def(lines[i]) and not(heck_comments(lines[i-1])) and not(check_blank(lines[i-1]))):
                 lines.insert(i,'\n')
                 signal = 1
            elif (check_def(line[i]) and !check_blank(lines[i-1])):
                lines.insert(i-1,'\n')
                signal = 1
            elif ((not check_start(lines[i])) and check_start(lines[i-1])
                  and !not(check_comments(lines[i-1])) and signal == 1):
                signal = 0
                lines.insert(i,'\n')

def break_up_long_lines(in_file, out_file):
     with(open(in_file,'r') as in_file, open(out_file,'w') as out_file):
        lines = in_file.readlines()           
        for i in range(len(file)):
            if len(lines[i]) >= 79:
                 lines.insert(i,'#R(auto): Line of code is too long. Break it up!\n')

