'''
Task 23
Written by Alex
'''





def prefix_counts(read_file):
    all_words = []
    for line in read_file:
        splited_line = line.split()
        for n in range(len(splited_line)):
            single_word = splited_line[n].lower()
            all_words.append(single_word)

    prefix_dict = {}
    

    for n in range(len(all_words)):
        word = all_words[n]
        if len(word) >= 3:
            if word[:3] in prefix_dict: 
                prefix_dict[word[:3]] += 1
            elif word[:3] not in prefix_dict:
                prefix_dict[word[:3]] = 1
    return prefix_dict

def main():

    file_name = 'letters_test.py'
    with open(file_name, 'r') as my_file:
        prefix = prefix_counts(my_file)

    freq = []
    for n in prefix:
        freq.append(prefix[n])
    freq = sorted(freq)

    first_common = ''
    for n in prefix:
        if prefix[n] == freq[-1]:
            first_common += n
            first_common += ', '
    print(first_common)

    


if __name__ == '__main__':
    main()



                
    
