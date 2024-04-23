



"""
Counts how many times each character appears in a file.

Read_file: A file open for reading

Returns: A dictionary similar to the one in the cereal tasks, where the keys
        are each character that occurs in the file. 
"""
def letter_counts(read_file):
    character_count = {}
    for line in read_file:
        for char in line:
            
            character_count[char] = char_counts.get(char, 0) + 1

    return char_counts
