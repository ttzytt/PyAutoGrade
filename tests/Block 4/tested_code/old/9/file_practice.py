




print('thank\nyou\t:)')


multiple_line_string = 'So\nmany\nlines of\ntext. Yay!'
lines = multiple_line_string.splitlines()

for count in range(len(lines)):
    print(lines[count])
    
print(len(lines))


sen = 'Nice to meet you'
sen = sen.split()

print(sen)
print(len(sen))


names = ['alex','lily','brian','harry']
names = ', '.join(names)

print(names)

lines = ['Here',
         'are',
         'multiple',
         'lines',
         'of',
         'text']
print(lines)
print('\n'.join(lines))
print(' '.join(lines))

file_name = 'Unit 2/alkanes.py'



with open(file_name, 'r') as my_file:
    list_of_lines = my_file.readlines()
lines_total = len(list_of_lines)


with open(file_name, 'r') as my_file: 
    character_count = 0
    for line in my_file: 
        character_count += len(line)


print('Total lines: ' + str(lines_total))
print('Total characters: ' + str(character_count))
print('Average characters per sentence: ' + str(character_count/lines_total))
print()
