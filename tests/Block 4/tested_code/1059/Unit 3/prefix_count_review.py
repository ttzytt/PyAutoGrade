










def letter_counts(read_file): 
    word_dictionary = {} 
    
    words = (read_file.read()).split() 
    for i in range (len(words)): 
        
        if len(words[i])>3: 
            if (words[i][0:3]) not in word_dictionary.keys():
                word_dictionary[words[i][0:3]] = 1 
            
            else:word_dictionary[words[i][0:3]] += 1 
    return(word_dictionary)






def main():
    with open('Text files/greeneggs.txt', 'r') as read_file:
        word_dictionary = letter_counts(read_file)
        
        most_common_prefix_string = '' 
        most_common_prefix_int = 0 
        second_most_common_prefix_string = '' 
        second_common_prefix_int = 0 


        for key in word_dictionary.keys():
            
            if word_dictionary[key] > most_common_prefix_int:
                
                second_most_common_prefix_string = most_common_prefix_string
                
                second_common_prefix_int = most_common_prefix_int
                most_common_prefix_string = key 
                most_common_prefix_int = word_dictionary[key]
                
            if word_dictionary[key] > second_common_prefix_int and key != most_common_prefix_string:
                
                second_most_common_prefix_string = key
                second_common_prefix_int = word_dictionary[key]
                
        print("The most common prefix is",most_common_prefix_string, "occurring",most_common_prefix_int, "times") 
        print("The next most common prefix is",second_most_common_prefix_string, "occurring",second_common_prefix_int, "times")

if __name__ == "__main__":
    main()
