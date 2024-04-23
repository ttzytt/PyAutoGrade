


import string

def prefix_counts(read_file, prefix_size = 3, punctuation_sensitive = False):
    prefixes = {}
    for line in read_file:
        if punctuation_sensitive:
            exclude = set(string.punctuation)
            line = ''.join(ch for ch in line if ch not in exclude)
        words = line.split()
        for word in words:
            if len(word) >= prefix_size:
                prefix = word[:prefix_size].lower()
                if prefix in prefixes:
                    prefixes[prefix] += 1
                else:
                    prefixes[prefix] = 1
    return prefixes

def main():
    num_to_print = 20
    
    with open('Text files/greeneggs.txt', 'r') as input_file:
        data = prefix_counts(input_file)

    
    maxes = [([''], 0) for _ in range(num_to_print)]
    for key, value in data.items():
        for i in range(num_to_print):
            if value > maxes[i][1]:                  
                for j in range(num_to_print-1,i,-1): 
                    maxes[j] = maxes[j-1]            
                maxes[i] = ([key], value)            
                break
            elif value == maxes[i][1]:
                maxes[i][0].append(key)              
                break                                
                                                     
    if any(i[1] == 0 for i in maxes):
        print("There aren't enough prefixes of different length to print. It'll print silly.")
            
    printing_string = ''
    for i in range(num_to_print):
        
        if i == 0:
            number_but_words = '1st'
        elif i == 1:
            number_but_words = '2nd'
        elif i == 2:
            number_but_words = '3rd'
        else:
            number_but_words = f'{i+1}th'

        
        multiple_string = f"prefix is  '{maxes[i][0][0]}'"
        if len(maxes[i][0]) > 1:
            multiple_string = 'prefixes are  '
            multiple_string += ', '.join(map(lambda x: f"'{x}'",maxes[i][0][:-1]))
            multiple_string += ' and ' + f"'{maxes[i][0][-1]}'"
        is_there_a_s = 's'
        if maxes[i][1] == 1:
            is_there_a_s = ''
        printing_string += (f"The {number_but_words} most occuring {multiple_string}," +
                            f"  with {maxes[i][1]} occurence{is_there_a_s}.\n")
    print(printing_string)            
    
if __name__ == '__main__':
    main()
