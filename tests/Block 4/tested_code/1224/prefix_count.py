


def prefix_counts(read_file):
    prefixes = {}
    with open(read_file, 'r') as my_file:
        for line in my_file:
            line = line.split()
            if len(line) > 0:
                if len(line[0]) >= 3:
                    if line[0][0:3] not in prefixes:
                        prefixes[line[0][0:3]] = 1
                    else:
                        prefixes[line[0][0:3]] += 1
    longest_len = 0
    for prefix in prefixes:
        if len(prefixes[prefix]) > longest_len:
            longest_len == prefixes[prefix]
    print('The most used prefix is' + prefixes[longest_len])
        
prefix_counts('Text Files/greeneggs.txt')
