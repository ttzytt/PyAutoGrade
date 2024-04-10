
def all_vowels_counter(read_file):
    vowels = 'aeiouAEIOU'
    count = 0
    for line in read_file:
        for letter in line:
            if letter in vowels:
                count += 1
    return count
        
       
        
        
file_name = 'Text files/names.txt'
with open(file_name, 'r') as my_file:
    list_of_lines = my_file.readlines()
    vowels = all_vowels_counter(list_of_lines)
print(vowels)



