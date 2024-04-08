


import random
possible_file = ['Text files/names.txt', 'Text files/addition.txt','Text files/greeneggs.txt','Text files/words.txt']
file_name = 'Text files/palindrom2.0.txt'

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
                
























