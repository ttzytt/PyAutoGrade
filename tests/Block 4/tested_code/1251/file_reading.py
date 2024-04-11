


import random
random.seed()



def average_length(file):
    
    result = 0
    
    count = 0
    for line in file:
        
        result += len(line)
        words = line.split()
        
        count += len(words)
    return result/count


def longest_word(file):
    result = []
    
    record = 0
    for line in file:
        words = line.split()
        for i in range(len(words)):
            if len(words[i]) >= record:
                
                record = len(words[i])
                
                result.append(words[i])
    final = []
    for i in range(len(result)):
        
        if len(result[i]) == record:
            final.append(result[i])
    return final


def longest_palindrome(file):
    result = []
    
    record = 0
    for line in file:
        words = line.split()
        
        for i in range(len(words)):
            temp = words[i].lower()
            
            if temp[::1]== temp[::-1] and len(words[i]) > record:
                
                record = len(words[i])
                
                result.append(words[i])
    final = []
    for i in range(len(result)):
        
        if len(result[i]) == record:
            final.append(result[i])
    return final



def all_vowels_counter(file):
    
    result = 0
    for line in file:
        words = line.split()
        for i in range(len(words)):
            
            signal = [0,0,0,0,0]
            for j in range(len(words[i])):
                if words[i][j].lower() == 'a':
                    signal[0] += 1
                elif words[i][j].lower() == 'e':
                    signal[1] += 1
                elif words[i][j].lower() == 'i':
                    signal[2] += 1
                elif words[i][j].lower() == 'o':
                    signal[3] += 1
                elif words[i][j].lower() == 'u':
                    signal[4] += 1
            
            if signal[0] * signal[1] * signal[2] * signal[3] * signal[4] != 0:
                result += 1
    return result 


def count_long_lines(file, min_length):
    result = 0
    for line in file:
         if len(line) >= min_length:
             result += 1
    return result


def random_word(file):
    
    record = []  
    
    for line in file:
        words = line.split()
        for i in range(len(words)):
            record.append(words[i])
    
    return random.choice(record)


def random_words(file, num_words):
    
    result =[]
    
    record = []  
    
    for line in file:
        words = line.split()
        for i in range(len(words)):
            record.append(words[i])
    
    for i in range(num_words):
        temp = random.choice(record)
        
        while temp in result:
            temp = random.choice(record)
        result.append(temp)
    return result


def specific_word_count(file, word):
    count = 0
    for line in file:
        words = line.split()
        
        for i in range(len(words)):
            if words[i].lower() == word.lower():
                count += 1
    return count


def starts_with_counter(file, word_beginning):
    count = 0
    for line in file:
        words = line.split()
        for i in range(len(words)):
            
            if words[i][:len(word_beginning)].lower() == word_beginning.lower():
                count += 1
    return count


def main():
    with open('Text files/words.txt','r') as in_file:
        print(average_length(in_file))
    with open('Text files/words.txt','r') as in_file:
        print(longest_word(in_file))
    with open('Text files/words.txt','r') as in_file:
        print(longest_palindrome(in_file))
    with open('Text files/words.txt','r') as in_file:
        print(all_vowels_counter(in_file))
    with open('Text files/words.txt','r') as in_file:
        print(random_word(in_file))
    with open('Text files/words.txt','r') as in_file:        
        print(random_words(in_file, 25))
    with open('Text files/words.txt','r') as in_file:    
        print(specific_word_count(in_file, 'apple'))
    with open('Text files/words.txt','r') as in_file:    
        print(starts_with_counter(in_file, 'ac'))


if __name__ == "__main__":
    main()





