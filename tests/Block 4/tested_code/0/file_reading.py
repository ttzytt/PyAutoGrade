import random


def average_length(read_file):
    total_length = 0
    total_words = 0
    for line in read_file:
        words = line.split()
        for word in words:
            total_length += len(words)
            total_words += 1
    if total_words == 0:
        return 0
    return total_length/total_words


def longest_word(read_file):
    long_words = []
    current_length = 0
    for line in read_file:
        words = line.split()
        for word in words:
            word_length = len(word)
            if word_length > current_length:
                long_words = [word]
                current_length = word_length
            elif word_length == current_length:
                long_words.append(word)
    return long_words


def longest_palindrome(read_file):
    longest_palindrome = []
    current_longest_length = 0
    for line in read_file:
        words = line.split()
        for word in words:
            if word == word[::-1]:
                word_length = len(word)
                if word_length > current_longest_length:
                    longest_palindrome = [word]
                    max_length = word_length
                elif max_length == word_length:
                    longest_palindrome.append(word)
    return longest_palindrome


def all_vowels_counter(read_file):
    vowels = ['a', 'e', 'i', 'o', 'u']
    count = 0
    for line in read_file:
        words = line.split()
        for word in words:
            for letter in word:
                if letter == 'a' and letter == 'e' and letter == 'i' and letter == 'o' and letter == 'u':
                    count += 1
    return count


def count_long_lines(read_file, min_length):
    count = 0
    for line in read_file:
        if len(line) >= min_length:
            count += 1
    return count


def random_word(read_file):
    words_list = []
    for line in read_file:
        words = line.split()
        words_list += words
    return random.choice(words_list)


def random_words(read_file, num_words):
    words_list = []
    random_list = []
    count = 0
    for line in read_file:
        words = line.split()
        words_list.append(words)
        while num_words > count:
            random_list.append(random.choice(words_list))
            count += 1
    return random_list


def specific_word_count(read_file, word):
    word_list = []
    count = 0
    for line in read_file:
        words = line.split()
        for specific_word in words:
            if specific_word == word:
                count += 1
    return count


def starts_with_counter(read_file, word_beginning):
    word_list = []
    count = 0
    for line in read_file:
        words = line.split()
        for word in words:
            if word[0] == word_beginning:
                count += 1
    return count
