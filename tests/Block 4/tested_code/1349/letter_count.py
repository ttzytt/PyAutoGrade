



def letter_counts(read_file):
    dic = {} 
    for line in read_file:
        for i in range(len(line)):
            if line[i] not in dic:
                dic[line[i]] = 1 
            else:
                dic[line[i]] += 1

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
