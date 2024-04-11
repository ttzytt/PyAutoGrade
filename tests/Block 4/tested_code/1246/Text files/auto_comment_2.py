def asdf(d):
    print(d)



def write_diamond_pattern(out_file_name, width):

    with open(out_file_name, 'w') as out_file:
        width += 1

        list_of_lines = []

        for i in range(1, width, 2):
            list_of_lines.append(' ' * ((width - (i+1))//2))
            list_of_lines.append('x' * i + '\n')

        for i in range(width - 3, 0, -2):
            list_of_lines.append(' ' * ((width - (i+1))//2))
            list_of_lines.append('x' * i + '\n')

        out_file.writelines(list_of_lines)





def last_name_first(in_file_name, out_file_name):

    with (open(in_file_name, 'r') as in_file,
              open(out_file_name, 'w') as out_file):
        
        for line in in_file:
            
            word_list = line.split()
            print(word_list)

            out_file.write(word_list[1] + ', ' + word_list[0] + '\n')

            




def blah_blah_blah(in_file_name, out_file_name):

    with (open(in_file_name, 'r') as in_file,
              open(out_file_name, 'w') as out_file):

        for line in in_file:

            if len(line) > 20:
                out_file.write(line[:15] + ', blah blah blah\n')
            else:
                out_file.write(line + '\n')
asdfasdf

def

def
def

out_file_name = 'Text files/diamond_pattern.txt'

write_diamond_pattern(out_file_name, 9)


in_file_name = 'Text files/names.txt'

out_file_name = 'Text files/names_reversed.txt'

last_name_first(in_file_name, out_file_name)


in_file_name = 'Text files/infection_function.txt'

out_file_name = 'Text files/infection_function_short.txt'

blah_blah_blah(in_file_name, out_file_name)
