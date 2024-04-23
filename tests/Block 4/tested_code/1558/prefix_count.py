





def prefix_counts(read_file):
    all_prefix_counts = {} 
    for line in read_file:
        words = line.split()
        for word in words: 
            if len(word[:3]) == 3:
                prefix = word[:3]
                if prefix in all_prefix_counts: 
                    all_prefix_counts[prefix] += 1
                else:
                    all_prefix_counts[prefix] = 1

    print(all_prefix_counts)
    return all_prefix_counts




def main():

    file_name_PC = 'Text files/short_word_list.txt' 
    with open(file_name_PC, 'r') as read_file:
        prefix_counts_results = prefix_counts(read_file)
                                   


    
if __name__ == "__main__":
    main()
