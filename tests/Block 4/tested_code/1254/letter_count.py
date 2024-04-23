


'''
Returns a dictionary where the keys are the characters in the file and it counts how many times each character
appears in a text file.
Inputs:
    read_file  A file open for reading
'''

def letter_counts(read_file):
    for line in read_file:
        for i in range(len(line)):
            
