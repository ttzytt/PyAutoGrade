









'''
Writes a “diamond” of x’s with the given width in a file.
For example, with width = 3, it should write
 x
xxx
 x
and with width = 5, it should write
  x
 xxx
xxxxx
 xxx
  x
    inputs:
        out_file    A file that is open for writing.
        width    An integer
        

'''
def write_diamond_pattern(out_file, width):
    for i in range(1, width, 2):
        
        for j in range(int((width-i) / 2)):
            out_file.write(' ')
        for j in range(i):
            out_file.write('x')
        out_file.write('\n')
        
    for i in range(width, 0, -2): 
        for j in range(int((width-i) / 2)):
            out_file.write(' ')
        for j in range(i):
            out_file.write('x')
        out_file.write('\n')




'''
Reads a file written in the form first_name last_name, and writes it in another
file in the form last_name, first_name
    inputs:
        out_file    A file that is open for writing.
        in_file    A file that is open for reading.
'''
def last_name_first(in_file, out_file):
    for line in in_file:
        words = line.split()
        out_file.write(words[len(words) - 1] + ', ')
        for i in range(len(words) - 1):
            out_file.write(words[i] + ' ')
        out_file.write('\n')




'''
Writes a file that contains solved addition problems read from another file.
    inputs:
        out_file    A file that is open for writing.
        in_file    A file that is open for reading.
'''
def add_and_write(in_file, out_file):
    for line in in_file:
        if(line[-1] == '\n'):
            line = line[:-1]
        words = line.split()
        answer = int(words[0]) + int(words[2])
        out_file.write(line + ' = ' + str(answer) + '\n')

        
'''
If line in input file is greater than 20, after first 15 charecters will be
replaced with string ', blah blah blah'
    inputs:
        out_file_name    A file name that will be opened for writing
        in_file_name    A file name that will be opened for reading
'''
def blah_blah_blah(in_file_name, out_file_name):
    with (open(in_file_name, 'r') as in_file,
        open(out_file_name, 'w') as out_file):
        for line in in_file:
            if (len(line) > 20):
                out_file.write(line[:15] + ', blah blah blah' + '\n')
            else:
                out_file.write(line)
        
    

    




def main():
    blah_blah_blah('Text files/bnw.txt', 'Text files/writingtestsfile.txt')


if __name__ == "__main__":
    main()

    
