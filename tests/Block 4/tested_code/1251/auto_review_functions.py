



type_1 = "'''"
type_2 = '"""'


def check_def(line):
    return (line[:4] == 'def ')


def check_comments (line):
    return ((line[0] == '#') or (line[:3] == type_1) or (line[:3] == type_2))


def check_blank(line):
    if line == '\n':
        return True
    for i in range(len(line)-1):
        if line[i] != ' ':
            return False
    return True


def check_start(line):
    return ((line[0] == ' ') and (not check_blank(line)))


def comments_for_functions(in_file, out_file):
    lines = in_file.readlines()
    if check_def(lines[0]):
        lines.insert(0,'#R(auto): Add a comment here that says what this function does!\n')
    for i in range(1,len(lines)):
        if (check_def(lines[i]) and (not check_comments(lines[i-1]))):
            lines.insert(i,'#R(auto): Add a comment here that says what this function does!\n')
    for i in range(len(lines)):
        out_file.write(lines[i])


def blank_lines_around_functions(in_file,out_file):
    lines = in_file.readlines()
    signal = 0
    for i in range(1,len(lines)):
        if check_def(lines[i]) and signal == 0:
            signal = 1
            if '#' in lines[i-1]:
                k = i - 1
                while(lines[k][0] == '#'):
                    k -= 1
                if (k > 0) and not (check_blank(lines[k])):
                    lines.insert(k+1,'\n')                
            elif (type_1 in lines[i-1]) or (type_2 in lines[i-1]): 
                k = i - 2
                while((type_1 not in lines[k]) and (type_2 not in lines[k])):
                    k -= 1
                if (k > 0) and not(check_blank(lines[k])):
                    lines.insert(k,'\n')
            elif not check_blank(lines[i-1]):
                lines.insert(i,'\n')
        elif ((check_start(lines[i-1])) and
            (not(check_blank(lines[i]))) and (not check_comments(lines[i])) and signal == 1):
            lines.insert(i,'\n')
            signal = 0

    for i in range(len(lines)):
        out_file.write(lines[i])

 
def break_up_long_lines(in_file, out_file):
        lines = in_file.readlines()
        i = 0
        while i < len(lines)-1:
            if len(lines[i]) >= 79:
                 lines.insert(i,'#R(auto): Line of code is too long. Break it up!\n')
                 i = i + 2
            else:
                i = i + 1
        if len(lines[len(lines)-1]) >= 79:
            lines.insert(len(lines)-1,'#R(auto): Line of code is too long. Break it up!\n')
        for i in range(len(lines)):
            out_file.write(lines[i])

            
def spaces_after_commas(in_file, out_file):
    lines = in_file.readlines()           
    for i in range(len(lines)):
        item = list(lines[i])
        for j in range(len(item)):
            if j != len(item)-1 and item[j] == ',' and item[j+1] != ' ':
                    item.insert(j+1 , ' ')
        lines[i] = ''.join(item)
        out_file.write(lines[i])


def main():
    with(open('test1.py','w') as out_file, open('test.py','r') as in_file):
        comments_for_functions(in_file, out_file)
    with(open('test2.py','w') as out_file, open('test.py','r') as in_file):
        blank_lines_around_functions(in_file,out_file)
    with(open('test3.py','w') as out_file, open('test.py','r') as in_file):
        break_up_long_lines(in_file, out_file)
    with(open('test4.py','w') as out_file, open('test.py','r') as in_file):
        spaces_after_commas(in_file, out_file)


if __name__ == "__main__":
    main()



            
            

