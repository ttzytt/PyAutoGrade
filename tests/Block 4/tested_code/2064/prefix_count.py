








'''
Returns a dictionary where the keys are all the 3-letter prefixes that occur
in the file, and the values are the number of times that prefix occurs. Not
case-sensitive
    input:
        read_file    A file that is open for reading.
'''
def prefix_counts(read_file):
    prefixes = {}
    for line in read_file:
        words = line.split()
        for word in words:
            if (len(word) > 2):
                word = word.lower()
                if word[:3] in prefixes:
                    prefixes[word[:3]] = prefixes[word[:3]] + 1

                else:
                    prefixes[word[:3]] = 1
    return prefixes


def common_prefixes(read_file):
    prefixes = prefix_counts(read_file)
    max_prefixes = []
    for prefix in prefixes:
        max_prefixes.append([prefixes[prefix], prefix])
    max_prefixes.sort()
    print(max_prefixes)
    
            
        
        







def main():
    file_name = 'Text files/workshopped_test_file.txt'
    with open(file_name, 'r') as my_file:
        common_prefixes(my_file)






if __name__ == "__main__":
    main()
    
