'''
Written by Alex
TASK 2-10
'''



import random
random.seed()

'''----------------------FUNCTIONS------------------------'''


def average_length(read_file):
    character_count = 0 
    word_count = 0
    for line in read_file:
        splited_line = line.split()
        word_count += len(splited_line) 
        for n in range(len(splited_line)):
            character_count += len(splited_line[n])
            
    return character_count/word_count
    



def longest_word(read_file):
    max_len = 0 
    long_words = []
    for line in read_file:
        splited_line = line.split()
        for n in range(len(splited_line)):
            word = splited_line[n]
            
            
            if word[-1] != ',' and word[-1] != '.':
                if len(word) > max_len:
                    max_len = len(word)
                    long_words = []
                    long_words.append(word)
                elif len(word) == max_len:
                    long_words.append(word)
                    
            else: 
                if len(word)-1 > max_len:
                    max_len = len(word)
                    long_words = []
                    long_words.append(word)
                elif len(word)-1 == max_len:
                    long_words.append(word)

    
    return long_words



def longest_palindrome(read_file):
    max_len = 0
    long_words = []
    for line in read_file:
        splited_line = line.split()
        for n in range(len(splited_line)):
            word = splited_line[n]

            if word == word[::-1]: 
            
                if word[-1] != ',' and word[-1] != '.':
                    if len(word) > max_len:
                        max_len = len(word)
                        long_words = []
                        long_words.append(word)
                    elif len(word) == max_len:
                        long_words.append(word)
                elif word[-1] == ',' or word[-1] == '.':
                    if len(word)-1 > max_len:
                        max_len = len(word)
                        long_words = []
                        long_words.append(word)
                    elif len(word)-1 == max_len:
                        long_words.append(word)
    return long_words      




def all_vowels_counter(read_file):
    all_vowels_words = []
    for line in read_file:
        splited_line = line.split()
        for n in range(len(splited_line)):
            word = splited_line[n]

            
            if ( ('A' in word or 'a' in word) and ('E' in word or 'e' in word) and ('I' in word or 'i' in word)
                 and ('O' in word or 'o' in word) and ('U' in word or 'u' in word) ):
                all_vowels_words.append(word)
    return all_vowels_words



def count_long_lines(read_file, min_length):
    long_lines = 0
    for line in read_file:
        characters_in_line = 0
        splited_line = line.split()
        for n in range(len(splited_line)):
            word = splited_line[n]
            
            for i in range(len(word)):
                if word[i] != ',' and word[i] != '.':
                    characters_in_line += 1
                    
        if characters_in_line >= min_length:
            long_lines += 1
    return long_lines



'''BE CAREFUL WITH LARGE FILES'''
def random_word(read_file):
    all_words = []
    for line in read_file:
        splited_line = line.split()
        for n in range(len(splited_line)):
            single_word = splited_line[n]
            all_words.append(single_word)
    
            
    length_of_file = len(all_words)
    position = random.randint(0, length_of_file - 1)
    if all_words[position][-1] == ',' or all_words[position][-1] == '.':
        all_words[position] == all_words[position][:-1]
        
        
    return all_words[position]
    



'''BE CAREFUL WITH LARGE FILES'''
def random_words(read_file,num_words):
    all_words = []
    random_words = []
    for line in read_file:
        splited_line = line.split()
        for n in range(len(splited_line)):
            single_word = splited_line[n]
            all_words.append(single_word)
    

    while len(random_words) < num_words:
    
        length = len(all_words)-1
        position = random.randint(0,length)
        if all_words[position][-1] == ',' or all_words[position][-1] == '.':
            all_words[position] == all_words[position][:-1]
            
        if all_words[position] not in random_words:
            random_words.append(all_words[position])
            
    return random_words
    



def specific_word_count(read_file, word):
    all_words = []
    appeared_time = 0
    for line in read_file:
        splited_line = line.split()
        for n in range(len(splited_line)):
            single_word = splited_line[n]
            if single_word[-1] == ',' or single_word[-1] == '.':
                single_word = single_word[:-1]
            all_words.append(single_word)
    

    for n in range(len(all_words)):
        if word.lower() == all_words[n].lower():
            appeared_time += 1
            

    return appeared_time




def starts_with_counter(read_file, word_beginning):
    all_words = []
    appeared_time = 0
    for line in read_file:
        splited_line = line.split()
        for n in range(len(splited_line)):
            single_word = splited_line[n]
            if single_word[-1] == ',' or single_word[-1] == '.':
                single_word = single_word[:-1]
            all_words.append(single_word)
    

    for n in range(len(all_words)):
        if len(all_words[n]) >= len(word_beginning):
        
        
            if all_words[n][:len(word_beginning)].lower() == word_beginning.lower():
            
                appeared_time += 1

    return appeared_time

'''------------------------TESTS-------------------------'''

def main():
    
    
    print('T2')
    file_name = 'Text files/names.txt'
    with open(file_name, 'r') as my_file:
        aver_len = average_length(my_file)
    print(aver_len)
    print()

    
    print('T3')
    file_name = 'Text files/names.txt'
    with open(file_name, 'r') as my_file:
        long_word = longest_word(my_file)
    print(long_word)
    print()

    
    print('T4')
    file_name = 'Text files/names.txt'
    with open(file_name, 'r') as my_file:
        long_palin = longest_palindrome(my_file)
    print(long_palin)
    print()

    
    print('T5')
    file_name = 'Text files/names.txt'
    with open(file_name, 'r') as my_file:
        all_vowels = all_vowels_counter(my_file)
    print(all_vowels)
    print()

    
    print('T6')
    file_name = 'Text files/names.txt'
    with open(file_name, 'r') as my_file:
        min_length = 10
        long_lines = count_long_lines(my_file, min_length)
    print(long_lines)
    print()

    
    print('T7')
    file_name = 'Text files/names.txt'
    with open(file_name, 'r') as my_file:
        rand_word = random_word(my_file)
    print(rand_word)
    print()

    
    print('T8')
    file_name = 'Text files/names.txt'
    with open(file_name, 'r') as my_file:
        num_words = 10
        rand_words = random_words(my_file,num_words)
    print(rand_words)
    print()

    
    print('T9')
    file_name = 'Text files/names.txt'
    with open(file_name, 'r') as my_file:
        word = 'li'
        appeared_time1 = specific_word_count(my_file, word)
    print(appeared_time1)
    print()

    
    print('T10')
    file_name = 'Text files/names.txt'
    with open(file_name, 'r') as my_file:
        word_beginning = 'li'
        appeared_time2 = starts_with_counter(my_file, word_beginning)
    print(appeared_time2)
    print()

if __name__ == '__main__':
    main()
