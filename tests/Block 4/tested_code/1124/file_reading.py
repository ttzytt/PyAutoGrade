



import random
random.seed()





def average_length(read_file):
    
    number_terms = 0
    total_length = 0
    
    for line in read_file:
        words = line.split()
        for word in words:
            total_length += len(word)
            number_terms += 1
    
    if number_terms == 0:
        return None
    
    return total_length/number_terms






def longest_word(read_file):
    
    list_longest_words = []
    len_longest_word = 0
    for line in read_file:
        
        words = line.split()
        for word in words:
            
            lowered_word = word.lower()
            
            
            if len(lowered_word) > len_longest_word:
                list_longest_words = [lowered_word]
                len_longest_word = len(lowered_word)
            
            elif len(word) == len_longest_word and not(word in list_longest_words):
                list_longest_words.append(word)
    return list_longest_words






def longest_palindrome(read_file):
    
    list_longest_palindromes = []
    len_longest_palindromes = 0
    
    for line in read_file:
        
        words = line.split()
        for word in words:
            
            lowered_word = word.lower()
            
            if lowered_word == lowered_word[::-1]:
                
                
                if len(lowered_word) > len_longest_palindromes:
                    list_longest_palindromes = [lowered_word]
                    len_longest_palindromes = len(lowered_word)
                
                elif len(lowered_word) == len_longest_palindromes and not(lowered_word in list_longest_palindromes):
                    list_longest_palindromes.append(lowered_word)
    return list_longest_palindromes






def all_vowels_counter(read_file):
    
    num_all_vowels = 0
    for line in read_file:
        
        words = line.split()
        for word in words:
            
            lowered_word = word.lower()
            
            if ('a' in lowered_word and 'e' in lowered_word and
                'i' in lowered_word and 'o' in lowered_word and 'u' in lowered_word):
                num_all_vowels += 1
    return num_all_vowels






def count_long_lines(read_file, min_length):
    
    num_long_lines = 0
    
    for line in read_file:
        print(line)
        
        
        if len(line) - 1 >= min_length:
            num_long_lines += 1
    return num_long_lines







def random_word(read_file):
    
    all_words = []
    
    for line in read_file:
        words = line.split()
        for word in words:
            all_words.append(word)
    
    return  random.choice(all_words)








def random_words(read_file, num_words):
    
    all_words = []
    
    random_words = []
    
    for line in read_file:
        words = line.split()
        for word in words:
            all_words.append(word)
    
    for _ in range(num_words):
        current_random = random.choice(all_words)
        random_words.append(current_random)
    return random_words    







def specific_word_count(read_file, word):
    
    num_times = 0
    
    for line in read_file:
        words = line.split()
        for current_word in words:
            
            lowered_word = current_word.lower()
            input_word = word.lower()
            if lowered_word == input_word:
                num_times += 1
    return num_times







def starts_with_counter(read_file, word_beginning):
    
    num_words = 0
    
    for line in read_file:
        words = line.split()
        for word in words:
            
            lowered_word = word.lower()
            
            if lowered_word[:len(word_beginning)] == word_beginning:
                num_words += 1
    return num_words



def main():
    file_name = 'Text files/greeneggs.txt'
    with open(file_name, 'r') as my_file:
        average_length_words = average_length(my_file)
        print('The file ' + file_name + ' contains ' + str(average_length_words) + ' as the average length.')
        print()
    file_name = 'Text files/greeneggs.txt'
    with open(file_name, 'r') as my_file:
        longest_words = longest_word(my_file)
        print('The file ' + file_name + ' contains ' + str(longest_words) + ' as the longest words.')
        print()
    file_name = 'Text files/commonwords.txt'
    with open(file_name, 'r') as my_file:
        longest_palindromes = longest_palindrome(my_file)
        print('The file ' + file_name + ' contains ' + str(longest_palindromes) + ' as the longest palindromes.')
        print()

    file_name = 'Text files/words.txt'
    with open(file_name, 'r') as my_file:
        num_all_vowels = all_vowels_counter(my_file)
        print('The file ' + file_name + ' contains ' + str(num_all_vowels) + ' as the number of words with all vowels.')
        print()

    file_name = 'Text files/test.txt'
    with open(file_name, 'r') as my_file:
        num_long_lines = count_long_lines(my_file, 5)
        print('The file ' + file_name + ' contains ' + str(num_long_lines) + ' as the number of long lines.')
        print()

    file_name = 'Text files/commonwords.txt'
    with open(file_name, 'r') as my_file:
        one_random_word = random_word(my_file)
        print('The file ' + file_name + ' contains ' + str(one_random_word) + ' as a random word.')
        print()

    file_name = 'Text files/commonwords.txt'
    with open(file_name, 'r') as my_file:
        list_random_words = random_words(my_file, 5)
        print('The file ' + file_name + ' contains ' + str(list_random_words) + ' as many random words.')
        print()

    file_name = 'Text files/greeneggs.txt'
    with open(file_name, 'r') as my_file:
        num_words = specific_word_count(my_file, 'eggs')
        print('The file ' + file_name + ' contains ' + str(num_words) + ' as the number of specific words.')
        print()

    file_name = 'Text files/names.txt'
    with open(file_name, 'r') as my_file:
        num_words_beginning = starts_with_counter(my_file, 'ap')
        print('The file ' + file_name + ' contains ' + str(num_words_beginning) + ' as' + 
              ' the number of words with a specific beginning.')
        print()

if __name__ == "__main__":
    main()
