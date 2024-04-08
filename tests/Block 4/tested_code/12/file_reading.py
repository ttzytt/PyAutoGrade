






def average_length(read_file):
        
    num_words = 0 
    num_letters = 0 
    
    for i in range(len(list_of_lines)): 

        line_of_words = list_of_lines[i].split()
        
        num_words += len(line_of_words)
        

        for j in range(len(line_of_words)):
            num_letters += len(line_of_words[j])
        
                    
    return(num_letters / num_words) 


file_name = 'Text files/greeneggs.txt'
with open(file_name, 'r') as my_file:
    
    
    list_of_lines = my_file.readlines()
    average_length = average_length(my_file)

print('The file ' + file_name + ' has on average ' + str(average_length)
      + ' characters in each word.')
print()




def longest_word(read_file):

    
    first_line_of_words = list_of_lines[0].split()
    
    long_words = [first_line_of_words[0]]
    

    for first_line_of_word in range(1, len(first_line_of_words)):
        
        if len(first_line_of_word) > len(long_words[-1]):
            long_words = [first_line_of_word]
            
        elif len(first_line_of_word) = len(long_words[-1]):
            long_words.append(first_line_of_word)
            

    
    for i in range(1, len(list_of_lines)): 
        line_of_words = list_of_lines[i].split()
        
        
        for line_of_word in range(len(line_of_words)):
            if len(line_of_word) > len(long_words[-1]):
                long_words = [line_of_word]
                
            elif len(line_of_word) = len(long_words[-1]):
                long_words.append(line_of_word)
                

    return(long_words)


file_name = 'Text files/greeneggs.txt'
with open(file_name, 'r') as my_file:
    
    
    list_of_lines = my_file.readlines()
    average_length = average_length(my_file)

print('The longest word in the file ' + file_name + ' has ' + (average_length)
      + ' characters.')
print()








































