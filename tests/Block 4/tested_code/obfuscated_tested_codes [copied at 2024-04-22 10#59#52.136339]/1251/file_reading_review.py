










import random
random.seed()




def average_length(read_file):
    with open(read_file,'r') as file:
        
        result = 0
        
        count = 0
        for line in file:
            
            result += len(line)
            words = line.split()
            
            count += len(words)
    return result/count


def longest_word(read_file):
    with open(read_file,'r') as file:
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


def longest_palindrome(read_file):
    with open(read_file,'r') as file:
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



def all_vowels_counter(read_file):
    
    result = 0
    with open(read_file,'r') as file:
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


def count_long_lines(read_file, min_length):
    result = 0
    with open(read_file,'r') as file:
        for line in file:
             if len(line) >= min_length:
                 result += 1
    return result


def random_word(read_file):
    
    record = []  
    with open(read_file,'r') as file:
        
        for line in file:
            words = line.split()
            for i in range(len(words)):
                record.append(words[i])
    
    return random.choice(record)


def random_words(read_file, num_words):
    
    result =[]
    
    record = []  
    with open(read_file,'r') as file:
        
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


def specific_word_count(read_file, word):
    count = 0
    with open(read_file,'r') as file:
        for line in file:
            words = line.split()
            
            for i in range(len(words)):
                if words[i].lower() == word.lower():
                    count += 1
    return count


def starts_with_counter(read_file, word_beginning):
    count = 0
    with open(read_file,'r') as file:
        for line in file:
            words = line.split()
            for i in range(len(words)):
                
                if words[i][:len(word_beginning)].lower() == word_beginning.lower():
                    count += 1
    return count


def main():
    print(average_length('Text files/words.txt'))
    print(longest_word('Text files/words.txt'))           
    print(longest_palindrome('Text files/words.txt'))
    print(all_vowels_counter('Text files/words.txt'))
    print(random_word('Text files/words.txt'))
    print(random_words('Text files/words.txt', 25))
    print(specific_word_count('Text files/names.txt', 'alex'))
    print(starts_with_counter('Text files/words.txt', 'ac'))


if __name__ == "__main__":
    main()





