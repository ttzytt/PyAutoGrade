






file_name = 'test_file.txt'

with open(file_name, 'r') as my_file:

    list_of_lines = my_file.readlines()
    print(list_of_lines)
    print()
    
    my_file.close()
