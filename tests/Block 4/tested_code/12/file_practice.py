



def count_characters(read_file):
    count = 0  
    for line in read_file:  
        count += len(line)
    return count


def made_backwards(line):
    return line[-1 : : -1]


file_name = 'Text files/greeneggs.txt'
with open(file_name, 'r') as my_file:
    num_characters = count_characters(my_file)

print('The file ' + file_name + ' contains ' + str(num_characters)
      + ' characters.')
print()


with open(file_name, 'r') as my_file:
    
    
    list_of_lines = my_file.readlines()
    line_one_backwards = made_backwards(list_of_lines[0])
    print(line_one_backwards)
    
