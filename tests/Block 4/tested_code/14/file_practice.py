



path_name = 'Text files/names.txt'

file = open(path_name)

full_content = file.read()


print(file.read() + '2')


print(full_content + '1')
print()


print(full_content[::])

file.close()

print()



path_name = 'Text files/names.txt'

with open(path_name, 'r') as file:
    full_content = file.read()

print(full_content)
print()
print(full_content[50:98])


print()

path_name = 'Text files/greeneggs.txt'
with open(path_name, 'r') as file:
    
    lines_list = file.readlines()

for i in range(len(lines_list)):
    print('Line ' + str((i + 1)) + ':' + ' ' + lines_list[i])

print()
with open(path_name, 'r') as file:
    character_count = 0

    for line in file:
        character_count += len(line)

print(str(character_count))
