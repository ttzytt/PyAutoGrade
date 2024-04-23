
file_name = 'Unit 2/alkenes.txt'
with open(file_name,'w') as my_file:
    alkene = 'methane, ethylene, propene'
    my_file.write(alkene)


input_file = 'Unit 2/alkanes.py'
output_file = 'Unit 2/alkenes.py'
with (open(input_file,'r') as in_file, open(output_file, 'w') as write_file):
    for line in in_file:
        splited_line = line.split()
        for n in range(len(splited_line)):
            alkane = splited_line[n]
            
            alkene = alkane[:-3] + 'e' + alkane[-2:]

            write_file.write(alkene)


input_file = 'Unit 2/alkanes.py'
output_file = 'Unit 2/alkenes.py'
with (open(input_file,'r') as in_file, open(output_file, 'w') as write_file):
    list_of_lines = in_file.readlines()
    for n in range(len(list_of_lines)):
        write_file.write(list_of_lines[n])


dick = {}
for n in range(0,11):
    dick[n] = n**2
print(dick)
print(len(dick))

user = input('Input your combinations of color(s): ')
user_key = user.split() 
total_num = 0
for n in range(len(user_key)):
    total_num += color_to_number[user_key[n]]
print('There are ' + str(total_num) + ' for total')

user = input('Input your combinations of color(s): ')
while user != 'quit':
    user_key = user.split()
    total_num = 0
    for n in range(len(user_key)):
        total_num += color_to_number[user_key[n]]
    print('There are ' + str(total_num) + ' for total')
    print()
    user = input('Input your combinations of color(s): ')
