



def prefix_counts(read_file):
    dic = {} 
    for line in read_file:
        words = line.split()
        for i in range(len(words)):
            if len(words[i]) < 3:
                continue
            if words[i][:3] not in dic:
                dic[words[i][:3]] = 1
            else:
                dic[words[i][:3]] += 1
    return dic





def main():
    in_file_name = 'Text files/names.txt'
    with (open(in_file_name, 'r') as read_file):
        letters = letter_counts(read_file) 

    for i in range(26):
        l = chr(ord('A')+i) 
        if l in letters:
            num = letters[l]
        else:
            num = 0 
        if chr(ord('a')+i) in letters:
            num += letters[chr(ord('a')+i)]
        print(l + ' ' + str(num)) 

    
if __name__ == "__main__":
    main()
