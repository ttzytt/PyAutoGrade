'''
Task 22
Written by Alex
'''




def letter_counts(read_file):
    
    letter_dict = {}
    letter_list = []
    
    for line in read_file:
        for n in range(len(line)):
            if line[n] in letter_list: 
                letter_dict[line[n]] += 1
            elif line[n] not in letter_list: 
                letter_list.append(line[n])
                letter_dict[line[n]] = 1
    return letter_dict


def main():

    file_name = 'Text files/names.txt'
    with open(file_name, 'r') as my_file:
        letters = letter_counts(my_file)
    
        
    for n in range(ord('A'),ord('A')+25):
        if chr(n) in letters and chr(n).lower() in letters:
            total_num = letters[chr(n)] + letters[chr(n).lower()]
        elif chr(n) in letters:
            total_num = letters[chr(n)]
        elif chr(n).lower() in letters:
            total_num = letters[chr(n).lower()]
        else:
            total_num = 0
        print(chr(n) + ' ' + str(total_num))

if __name__ == '__main__':
    main()
