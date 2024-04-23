





"""
T22 part a
 
Creates a dictionary with every letter (both upper and lower) and character from a text file
and returns the dictionary.

inputs:
            read_file                a file open for reading
"""
def letter_counts(read_file):
    all_letter_counts = {} 
    for line in read_file:
        words = line.split()
        for word in words: 
            
            for i in range(len(word)):
                if word[i] in all_letter_counts: 
                    all_letter_counts[word[i]] += 1
                else:
                    all_letter_counts[word[i]] = 1
    
    return all_letter_counts


        
        
    




def main():

    file_name_LC = 'Text files/words.txt' 
    with open(file_name_LC, 'r') as read_file:
        letter_counts_results = letter_counts(read_file)


        """
        T22 part b
        Prints the count of every letter in the dictinary (not case specific- printed as upper
        case)
        """
        letter = 'A'
        while letter <= 'Z': 
            if letter not in letter_counts_results:
                letter_counts_results[letter] = 0
            print(letter, (letter_counts_results[letter] + 
                                                           
                           
                           letter_counts_results[letter.lower()] ))
            letter = chr(ord(letter) + 1) 
                                          
                                          


    
if __name__ == "__main__":
    main()






