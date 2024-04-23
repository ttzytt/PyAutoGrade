



def count_characters(read_file):
    count = 0
    for line in read_file:
        count = count + len(line)
    return count

file_name = 'Text files/names.txt'
with open(file_name, 'r') as my_file:
    num_characters = count_characters(my_file)

print('The file ' + file_name + ' contains ' + str(num_characters)
      + ' characters.')
print()



def count_lines(read_file):
    lines = read_file.read().splitlines()
    return len(lines)

file_name = 'Text files/names.txt'
with open(file_name,'r') as my_file:
    
    lines_counted = count_lines(my_file)

print('The file ' + file_name + ' contains ' + str(lines_counted)
      + ' lines.')
print()



