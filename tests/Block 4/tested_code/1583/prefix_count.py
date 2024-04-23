









def prefix_counts(read_file, prefix_size = 3):
    prefix_nums = {}

    
    for line in read_file:
        line = line.split()
        
        for word in line:
            word = word.lower()
            if len(word) >= prefix_size:
                if word[:prefix_size] not in prefix_nums:
                    prefix_nums[word[:prefix_size]] = 1
                else:
                    prefix_nums[word[:prefix_size]] += 1

    return prefix_nums








def main(num_to_print = 2):

    
    with open('Text files/names.txt', 'r') as my_file:
        prefix_nums = prefix_counts(my_file, 3)


    
    keys = list(prefix_nums.keys())
    changes = 1
    while changes > 0:
        changes = 0
        for i in range(len(keys) - 1):
            if prefix_nums[keys[i]] < prefix_nums[keys[i + 1]]:
                keys[i], keys[i + 1] = keys[i + 1], keys[i]
                changes += 1

    
    current_prefix_index = 0
    for i in range(num_to_print): 

        if current_prefix_index >= len(keys):
            print('There are no more prefixes! You ate them all!')
            break
        else:
            prefixes_to_print = [keys[current_prefix_index]]
            
            
            while (current_prefix_index + 1 < len(keys)
                   and prefix_nums[keys[current_prefix_index]]
                   == prefix_nums[keys[current_prefix_index + 1]]):
                
                prefixes_to_print.append(keys[current_prefix_index+1])
                current_prefix_index += 1

            
            if len(prefixes_to_print) == 1: 
                print('The #' + str(i+1) + ' common prefix is "'
                      + prefixes_to_print[0] + '", occuring '
                      + str(prefix_nums[prefixes_to_print[0]])
                      + ' times.')
            else: 
                print('The #' + str(i+1) + ' common prefixes are "'
                      + '", "'.join(prefixes_to_print) + '", occuring '
                      + str(prefix_nums[prefixes_to_print[0]])
                      + ' times.')

            current_prefix_index += 1


    
    '''
    most_common_prefix = keys[0]
    next_common_prefix = keys[0]
    for prefix in prefix_nums:
        if prefix_nums[prefix] > prefix_nums[most_common_prefix]:
            next_common_prefix = most_common_prefix
            most_common_prefix = prefix
        elif prefix_nums[prefix] > prefix_nums[next_common_prefix]:
            next_common_prefix = prefix
    
    print('The most common prefix is "' + most_common_prefix
          + '", occurring ' + str(prefix_nums[most_common_prefix]) + ' times.')
    print('The next most common prefix is "' + next_common_prefix
          + '", occurring ' + str(prefix_nums[next_common_prefix]) + ' times.')
    '''


if __name__ == "__main__":
    main(10)
    
