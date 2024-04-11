



lista = (['hloloh','hoho'],['ha'],['wuwu'])
listb = ('halo', 'ha', 'wuwu')
number1 = '122 '
file_name = 'Text files/greeneggs.txt'
opened_file = open(file_name, 'r')

with open(file_name,'r') as myy_file:
    full_content = myy_file.read()
    print(full_content[:100])

with open(file_name,'r') as my_file:
    list_of_lines = my_file.readlines()
print('Line 4 says: ' + list_of_lines[4])


def count_characters(read_file):
    count = 0  
    for line in read_file:
        count += len(line)
    return count

def count_char_without_space(read_file):
    count = 0  
    for line in read_file:
        for words in line:
            if words != ' ':
                count += 1
    return count

with open(file_name, 'r') as my_file:
    num_characters = count_characters(my_file)

with open(file_name, 'r') as my_file: 
    num_words = count_char_without_space(my_file)

    print(num_characters)
    print(num_words)

