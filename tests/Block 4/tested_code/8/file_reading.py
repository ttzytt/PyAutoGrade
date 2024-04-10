



import random









def average_length(read_file):
    word_len_sum = 0
    num_words = 0
    for line in read_file:
        words = line.split()
        for word in words:
            word_len_sum = word_len_sum + len(word)
            num_words += 1
    return word_len_sum / num_words




def longest_word(read_file):
    long_word = ' '
    current_word = ' '
    old_word = ' '
    for line in read_file:
        words = line.split()
        for word in words:
            current_word = word
            if len(current_word) > len(old_word):
                long_word = current_word
            old_word = current_word
            
    return long_word



def longest_palindrome(read_file):
    current_palindrome = ''
    old_palindrome = ''
    longest_palindrome_list = []
    for line in read_file:
        words = line.split()
        line.lower()
        for word in words:
            
            if word == word[::-1]:
                current_palindrome = word

            if len(current_palindrome) > len(old_palindrome):
                longest_palindrome_list.append(current_palindrome)
                
            old_palindrome = current_palindrome

    for i in range(len(longest_palindrome_list)):
        if len(longest_palindrome_list[i]) > len(longest_palindrome_list[i - 1]):
            true_longest_palindrome = longest_palindrome_list[i]
    return true_longest_palindrome





def all_vowels_counter(read_file):
    
    for line in read_file:
        words = line.split()
        
        amount_a = 0
        amount_e = 0
        amount_i = 0
        amount_o = 0
        amount_u = 0
        all_vowels = 0
            
        for word in words:
            
            for letter in word:
                if letter == 'a':
                    amount_a += 1
                elif letter == 'e':
                    amount_e += 1
                elif letter == 'i':
                    amount_i += 1
                elif letter == 'o':
                    amount_o += 1
                elif letter == 'u':
                     amount_u += 1
            if amount_a > 0 and amount_e > 0 and amount_i > 0 and amount_o > 0 and amount_u > 0:
                all_vowels += 1
                
        return all_vowels




def count_long_lines(read_file, min_length):
    amount_greater = 0
    for line in read_file:
        words = line.split()
        for word in words:
            
            character = 0
            for letter in word:
                character += 1
        if character >= min_length:
            amount_greater += 1
    return amount_greater



def random_word(read_file):
    word_list = []
    for line in read_file:
        line.split()
        word_list.append(line)
    
    random_num = random.randint(0, len(word_list))
    return word_list[random_num]



def random_words(read_file, num_words):
    word_list = []
    return_list = []
    for line in read_file:
        line.split()
        word_list.append(line)
    for i in range(num_words):
        random_num = random.randint(0, len(word_list))
        return_list.append(word_list[random_num])
    return return_list



def specific_word_count(read_file, specific_word):
    amount_of_same_words = 0
    for line in read_file:
        words = line.split()
        for word in words:
            if word == specific_word:
                amount_of_same_words += 1
    return amount_of_same_words



def starts_with_counter(read_file, word_beginning):
    num_beginning = 0
    for line in my_file:
        words = line.split()
        for word in words:
            if word[0] == word_beginning:
                num_beginning += 1
    return num_beginning








def main():
    file_name = 'Text files/commonwords.txt'
    
    with open(file_name, 'r') as my_file:
        average_len = average_length(my_file)
        

    print('The average word length in ' + file_name + ' is ' + str(average_len)
          + ' characters.')
    print()

    my_file.close()


    with open(file_name, 'r') as my_file:
        longest = longest_word(my_file)
        
    print('The longest word in ' + file_name + ' is ' + str(longest)
          + '.')
    print()
    my_file.close()


    with open(file_name, 'r') as my_file:

        palindrome = longest_palindrome(my_file)

    print('The longest palindrome in ' + file_name + ' is ' + str(palindrome)
          + '.')
    print()
    my_file.close()


    with open(file_name, 'r') as my_file:

        vowels_counter = all_vowels_counter(my_file)

    print('The amount of words with all the vowels in ' + file_name + ' is ' + str(vowels_counter)
          + '.')
    print()
    my_file.close()


    min_length = int(input("Minimum length: "))
    with open(file_name, 'r') as my_file:
        long_lines = count_long_lines(my_file, min_length)
    print('The amount of lines with length > ' + str(min_length) + ' In the file ' + file_name + ' is ' + str(long_lines)
          + '.')
    print()
    my_file.close()


    with open(file_name, 'r') as my_file:

        word = random_word(my_file)

    print('A random word in ' + file_name + ' is ' + str(word) + '.')
    print()
    my_file.close()


    num_words = int(input('How many words?'))
    with open(file_name, 'r') as my_file:

        words = random_words(my_file,num_words)

    print(str(num_words) + ' random words in ' + file_name + ' are ' + str(words) + '.')
    print()
    my_file.close()


    specific_word = str(input('What word?'))
    with open(file_name, 'r') as my_file:

        word_count = specific_word_count(my_file,specific_word)

    print('The amount of the word ' + str(specific_word) + ' in ' + file_name + ' is ' + str(word_count) + '.')
    print()
    my_file.close()


    word_beginning = str(input('Starting character: '))
    with open(file_name, 'r') as my_file:

        starts_with = starts_with_counter(my_file,word_beginning)

    print('The amount of words that start with ' + str(word_beginning) + ' in ' + file_name + ' is ' + str(starts_with) + '.')
    print()
    my_file.close()

if __name__ == "__main__":
    main()
