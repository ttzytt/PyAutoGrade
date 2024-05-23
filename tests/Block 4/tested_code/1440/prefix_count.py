




def prefix_counts(read_file,prefix_size = 3):
    prefix = {}
    for line in my_file: 
        words = line.split()
        for i in range(len(words)):
            lowered = words[i].lower()
            if len(lowered) >= prefix_size:
                if lowered[:prefix_size] not in prefix:
                    prefix[lowered[:prefix_size]] = 1
                else:
                    prefix[lowered[:prefix_size]] += 1
                    
    first_common = 0
    sec_common = 0
    first_common_word = ''
    
    for i in prefix:
        if prefix[i] >= first_common:
            sec_common = first_common
            first_common = prefix[i]
            sec_common_word = first_common_word
            first_common_word = i
    
    
    
    if first_common == sec_common: 
        print(f'there are two most common prefix.')
        print(f'they are "{first_common_word}" and "{sec_common_word}", occurring both {first_common} times.')
    else:
        print(f'the most common prefix is: "{first_common_word}", occurring {first_common} times.')
        print(f'the next most common prefix is: "{sec_common_word}", occurring {sec_common} times.')


read_file = 'Text files/words.txt'
with (open(read_file,'r') as my_file): 
    prefix_counts(read_file)


