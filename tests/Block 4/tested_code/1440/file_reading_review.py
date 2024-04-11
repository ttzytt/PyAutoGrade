





import random
possible_file = ['Text files/aeiou.txt','Text files/names.txt', 'Text files/addition.txt','Text files/greeneggs.txt','Text files/words.txt']
file_name = random.choice(possible_file)

print(file_name)



def average_length():
    with open(file_name, 'r') as my_file:
        word_count = 0
        words_count = 0
        for line in my_file:
            words = line.split()
            word_count += len(words)
            for i in range(len(words)):
                words_count += len(words[i])
            avg_count = words_count/word_count
    print(f'The average lenth of words in the file_read is {round(avg_count,2)}')


average_length()





def longest_word():
    with open(file_name, 'r') as my_file:
        a = 0
        longest_words = []
        for line in my_file:
            words = line.split()
            for i in range(len(words)):
                if len(words[i]) >= a :
                    a = len(words[i])
                    b = words[i]

    with open(file_name, 'r') as my_file:
        for line in my_file:
            words = line.split()
            for i in range(len(words)):
                if len(words[i]) == a:
                    longest_words.append(words[i])
    return longest_words
            




def longest_palindrome():
    with open(file_name, 'r') as my_file:
        length = 0
        for line in my_file:
            words = line.split()
            for i in range(len(words)):
                if words[i][::-1] == words[i]:
                    for_now = words[i]
                if len(words[i]) > length:
                    length = len(words[i])
        print(length)
        print(for_now)
                







def all_vowels_counter():
    current_word = []
    with open(file_name,'r') as my_file:
        for line in my_file:
            words = line.split()
            lowered_words = []
            for i in range(len(words)): 
                lower_word = words[i].lower()
                lowered_words.append(lower_word)
            for i in range(len(lowered_words)):
                if 'a' and 'e' and 'i' and 'o' and 'u' in lowered_words[i]:
                    current_word.append(lowered_words[i])
    print(current_word)






def count_long_lines(file_name, min_length):
    length = 0
    number_success = 0
    with open(file_name,'r') as my_file:
        for line in my_file:
            words = line.split()
            for i in range(len(words)):
                length += len(words[i])
            if length >= min_length:
                number_success += 1
    return number_success
            



def random_word(file_name):
    with open(file_name,'r') as my_file:
        list_of_lines = my_file.readlines()
        random_word = random.choice(list_of_lines)
        while random_word == '\n':
            random_word = random.choice(list_of_lines)
        while random_word != '\n' and '\n' in random_word:
            random_word = random_word[:len(random_word)-2]
            words = random_word.split()
            random_word1 = random.choice(words)
    return random_word1




def random_words_2(file_name, num_words):
    
   with open(file_name,'r') as my_file:
       all_word = []
       random_words = []
       for line in my_file:
           words = line.split()
           for i in range(len(words)):
               all_word.append(words[i])
       for i in range(num_words):
           random_word = random.choice(all_word)
           random_words.append(random_word)
       return random_words





def specific_with_count(file_name, word):
    count = 0
    with open(file_name,'r') as my_file:
        for line in my_file:
            words = line.split()
            for i in range(len(words)):
                if word == words[i]:
                    count += 1
    return count




def starts_with_counter(read_file, word_begin):
    count = 0
    with open(file_name,'r') as my_file:
        list_lines = my_file.readlines()
        for i in range(len(list_lines)):
            if list_lines[i][:len(word_begin)] == word_begin:
                
                count += 1
    return count
    
                
        










