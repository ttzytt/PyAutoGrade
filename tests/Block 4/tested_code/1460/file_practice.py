


file_name = 'Text files/names.txt'


def count_e(read_file):
    count = 0
    for char in read_file:
        if char == 'e':
            count += 1
    return count


with open(file_name, 'r') as my_file:
    num_characters = count_e(my_file)

print('The file ' + file_name + ' contains ' + str(num_characters)
      + ' e's.')
print()

