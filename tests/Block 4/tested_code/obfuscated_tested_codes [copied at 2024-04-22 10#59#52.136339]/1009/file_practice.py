


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


names = [
    'Lisa Goliyad',
    'Derek Li',
    'Vivian Li',
    'Echo Ma',
    'Tom Qiu',
    'Jeffrey Yang',
    'Annie Ye',
    'Amy (Yihan) Chen',
    'Rachel Wang',
    'Gracie Anghelescu',
    'Ethan Che',
    'Kaylee Gordon',
    'David Hsu',
    'Sam Kemp',
    'Arun Pratik',
    'Maggie Rao',
    'William Pearce',
    'Jessie Wang',
    'Frank Wang',
    'Mark Zhao',
    'Alex Zhu',
    'Maya Fey',
    'Sky Hu',
    'Austin Huang',
    'Albert Zhao',
    'Daniel Rashidi',
    'Joy Wu',
    'Valentine Liu',
    'Qixiang Feng'
]



for name in names:
    last_name = name.split()[-1] 
    print (last_name)
