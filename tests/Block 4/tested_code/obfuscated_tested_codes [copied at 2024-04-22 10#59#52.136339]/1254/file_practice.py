




file_name = 'Text files/words.txt'
with open(file_name, 'r') as my_file:
    
    list_of_lines = my_file.readlines()
    
    for i in range (len(list_of_lines)):
        
        if list_of_lines[i][1:3] == 'ue':
            
            print (list_of_lines[i])

'''
This code checks all the words in the 'words' file
and prints out all the words that have the second and third letter being 'ue'

'''
