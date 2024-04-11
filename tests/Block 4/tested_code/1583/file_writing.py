










def write_diamond_pattern(out_file, width):
    
    list_of_lines = []

    num_spaces = 0
    num_xs = 0

    
    for i in range(int((width - 1) / 2)):
        num_spaces = int(((width - 1 - (2 * i)) / 2))
        num_xs = 1 + 2 * i
        row = ' ' * num_spaces
        row += 'x' * num_xs
        row += '\n'
        list_of_lines.append(row)

    
    for i in range(int((width + 1) / 2) - 1, -1, -1):
        num_spaces = int(((width - 1 - (2 * i)) / 2))
        num_xs = 1 + 2 * i
        row = ' ' * num_spaces
        row += 'x' * num_xs
        row += '\n'
        list_of_lines.append(row)

        
    out_file.writelines(list_of_lines)











def last_name_first(in_file, out_file):
    for line in in_file:
        line = line.split()

        converted_name = line[1] + ', ' + line[0] + '\n'

        out_file.write(converted_name)












def add_and_write(in_file, out_file):
    for line in in_file:
        line = line.split()

        
        answer = int(line[0]) + int(line[-1])

        
        
        processed_line = (line[0] + ' + ' + line[-1] + ' = ' + str(answer)
                          + '\n')

        out_file.write(processed_line)










def blah_blah_blah(in_file_name, out_file_name):
    with (open(in_file_name, 'r') as in_file,
      open(out_file_name, 'w') as out_file):
        
        for line in in_file:
            if len(line) > 20:
                write_line = line[:15] + ', blah blah blah' + '\n'
            else:
                write_line = line

            out_file.write(write_line)




def main():
    with open('Text files/diamond.txt', 'w') as out_file:
        write_diamond_pattern(out_file, 11)
        

    with (open('Text files/names.txt', 'r') as in_file,
      open('Text files/lastnamesfirst.txt', 'w') as out_file):
      last_name_first(in_file, out_file)


    with (open('Text files/addition.txt', 'r') as in_file,
      open('Text files/additionanswerkey.txt', 'w') as out_file):
      add_and_write(in_file, out_file)

        
    blah_blah_blah('Text files/greeneggs.txt', 'Text files/blaheggs.txt')         


if __name__ == "__main__":
    main()
  

        


      

        

