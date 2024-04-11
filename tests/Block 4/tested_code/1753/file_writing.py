





'''
Suppose out_file is a file open for writing and width is a positive odd integer. This function
should print a “diamond” of x’s with the given width. For example, with width = 3, it should write
 x
xxx
 x
to the file and with width = 5, it should write
  x
 xxx
xxxxx
 xxx
  x
to the file.

    inputs:
        in_file    A file that is open for reading.
        out_file   A file that is open for writing
'''
def write_diamond_pattern(out_file, width):

    for i in range(1, width + 1, 2):
        spaces = (width - i)//2
        string = (spaces * ' ') + i * 'x'
        out_file.write(string)
        out_file.write('\n')

    for i in range(width - 2, 0, -2):
        spaces = (width - i)//2
        string = (spaces * ' ') + i * 'x'
        out_file.write(string)
        out_file.write('\n')




'''
Returns a file that has everyboone's name in the format last name, first name
    inputs:
        in_file    A file that is open for reading.
        out_file   A file that is open for writing
'''
def last_name_first(in_file, out_file):

    for line in in_file:
        words = line.split()
        out_file.write(words[1])
        out_file.write(', ')
        out_file.write(words[0])
        out_file.write('\n')



        
'''
Returns a file that has the addition problem given as well as the result
    inputs:
        in_file    A file that is open for reading.
        out_file   A file that is open for writing
'''

def add_and_write(in_file, out_file):
    for line in in_file:
        nums = line.split()
        result = 0
        for i in range(len(nums)):
            if nums[i] != '+' and nums[i] != ' +' and nums[i] != '+ ' and nums[i] != ' + ':
                result = result + int(nums[i])
        out_file.write(line[0:-1])
        out_file.write(' = ')
        out_file.write(str(result))
        out_file.write('\n')

'''
Returns a file that has the addition problem given as well as the result
    inputs:
        in_file    A file that is open for reading.
        out_file   A file that is open for writing
'''
def blah_blah_blah(in_file_name, out_file_name):
    with (open(in_file_name, 'r') as in_file,
            open(out_file_name, 'w') as out_file):
        for line in in_file:
            if len(line) > 20:
                line = line[:15] + ', blah blah blah\n'
                out_file.write(line)
            else:
                out_file.write(line)








#------------------------------------------ Main ----------------------------------------------

def main():

    out_file_name = 'Text files/diamonds.txt'
    with open(out_file_name, 'w') as out_file:
        write_diamond_pattern(out_file, 9)
          

        
    in_file_name = 'Text files/names.txt'
    out_file_name = 'Text files/last_first_names.txt'

    ## We can open 2 files in a single with statement.
    ## We use parentheses for this simply because the stament is too long to
    ## fit on one line.
    with (open(in_file_name, 'r') as in_file,
            open(out_file_name, 'w') as out_file):
        last_name_first(in_file, out_file)  ## Write it to out_file

        

    in_file_name = 'Text files/addition.txt'
    out_file_name = 'Text files/sum.txt'

    with (open(in_file_name, 'r') as in_file,
            open(out_file_name, 'w') as out_file):
        add_and_write(in_file, out_file)  ## Write it to out_file




    in_file_name = 'Text files/greeneggs.txt'
    out_file_name = 'Text files/short_greeneggs.txt'
    blah_blah_blah(in_file_name, out_file_name)


if __name__ == "__main__":
    main()
    
