

read_file = 'Text files/palindrom2.0.txt'

def prefix_counts(read_file):
    prefix = {}
    for line in my_file:
        words = line.split()
        for i in range(len(words)):
            lowered = words[i].lower()
            if len(lowered) >= 3:
                if lowered[:3] not in prefix:
                    prefix[lowered[:3]] = 1
                else:
                    prefix[lowered[:3]] += 1
    print(prefix)
    first_common = 0
    sec_common = 0
    for i in prefix:
        if prefix[i] >= first_common:
            sec_common = first_common
            first_common = prefix[i]
    print(sec_common)
    print(first_common)
    
with (open(read_file,'r') as my_file): 
    prefix_counts(read_file)
