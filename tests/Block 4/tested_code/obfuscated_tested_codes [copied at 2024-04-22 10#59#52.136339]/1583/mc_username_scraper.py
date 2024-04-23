def scrape_words(read_file, characters):
    return_words = []
    for line in read_file:

        if len(line) == characters and line[0] == 'g':
            return_words.append(line)

        if len(return_words) > 60:
            break

    return return_words

words = 'Text files/words.txt'
with open(words, 'r') as my_file:
    print(scrape_words(my_file, 16))
          
        
    
