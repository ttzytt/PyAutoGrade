




def count_a_word(string):

    word_counter = 0

    file_name = 'Text files/greeneggs.txt'
    with open(file_name, 'r') as my_file:
        contents = my_file.read()

    
    delimiters = [',', '-', '.', '!', ' ', '?']
    for delimiter in delimiters:
        
        contents = " ".join(contents.split(delimiter))
     
    words = contents.split()

    for word in words:
        if word == string:
            word_counter += 1

    return word_counter



while True:
    input_word = input('What word would you like to count? ')
    
    print('The word ' + input_word + ' appears ' + str(count_a_word(input_word))
          + ' times.')




