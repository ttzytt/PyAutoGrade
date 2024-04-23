


'''
Returns the number of characters in the file.
    inputs:
        read_file    A file that is open for reading.
'''
def count_characters(read_file):
    count = 0  
    for line in read_file:  
        count += len(line)
    return count


file_name = 'Text files/names.txt'
with open(file_name, 'r') as my_file:
    num_characters = count_characters(my_file)

print('The file ' + file_name + ' contains ' + str(num_characters)
      + ' characters.')
print()



file_name = 'Text files/names.txt'
with open(file_name, 'r') as my_file:
    
    
    names = my_file.readlines()



for name in names:
    last_name = name.split()[-1] 
    print (last_name)
