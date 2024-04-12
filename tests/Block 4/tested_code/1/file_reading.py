from io import StringIO
import random
def average_length(read_file):
    total_length = 0
    total_words = 0
    # Iterate over each line in the file
    for line in read_file:
        # Split the line into words
        words = line.split()
        # Update total words count
        total_words += len(words)
        # Update total length count by summing the lengths of each word
        total_length += sum(len(word) for word in words)

    # Calculate the average length
    if total_words > 0:
        average_length = total_length / total_words
    else:
        average_length = None  # Handle the case when there are no words in the file
    read_file.seek(0)
    return average_length

def longest_word(read_file):
    longest_words = []
    max_length = 0
    # Iterate over each line in the file
    for line in read_file:
        # Split the line into words
        words = line.split()
        # Iterate over each word in the line
        for word in words:
            word = word.lower()
            if len(word) > max_length:
                max_length = len(word)
                longest_words = [word]
            elif len(word) == max_length and word not in longest_words:
                # If the current word has the same length as the longest word, add it to the list
                longest_words.append(word)
    read_file.seek(0)
    return longest_words
    
def longest_palindrome(read_file):
    longest_palindromes = []
    max_length = 0

    for line in read_file:
        words = line.split()
        
        for word in words:
            # Check if the word is a palindrome
            word = word.lower()
            if word == word[::-1]:
                # If the word is a palindrome and its length is greater than the current maximum length
                if len(word) > max_length:
                    max_length = len(word)
                    longest_palindromes = [word]
                elif len(word) == max_length and word not in longest_palindromes:
                    # If the word is a palindrome and its length is equal to the current maximum length
                    longest_palindromes.append(word)
    read_file.seek(0)
    return longest_palindromes

def all_vowels_counter(read_file):
    count = 0
    
    for line in read_file:
        words = line.split()
        
        for word in words:
            # Convert the word to lowercase for case-insensitive comparison
            word_lower = word.lower()
            # Check if all vowels are present in the word
            if 'a' in word_lower and 'e' in word_lower and 'i' in word_lower and 'o' in word_lower and 'u' in word_lower:
                count += 1
    read_file.seek(0)
    return count

def count_long_lines(read_file, min_length):
    num_long_lines = 0

    for line in read_file:
        # Check if the length of the line is at least min_length
        if len(line) >= min_length:
            num_long_lines += 1
    read_file.seek(0)
    return num_long_lines

def random_word(read_file):
    words = read_file.read()
    word_list = words.split()
    random_word = random.randint(0, len(word_list) - 1)
    return word_list[random_word]

def random_words(read_file, num_words):
    words = read_file.read()
    word_list = words.split()
    random_words_list = []
    for i in range(num_words):
        random_words_list.append(word_list[random.randint(0, len(word_list) - 1)])
    return random_words_list

def specific_word_count(read_file, word):
    count = 0
    word = word.lower()
    for line in read_file:
        # Split the line into words
        words = line.split()
        words = [w.lower() for w in words]
        # Count occurrences of the target word
        count += words.count(word)
    return count


def starts_with_counter(read_file, word_beginning):
    count = 0
    for line in read_file:
        # Split the line into words
        words = line.split()
        words = [w.lower() for w in words]
        # Count words that start with the specified prefix
        count += sum(1 for word in words if word.startswith(word_beginning))
    return count
