


import random

def prefix_counts(read_file):

    prefix_counts = {}

    for line in read_file:
        
        line = line.lower()

        line = line.split()

        

        for word in line:
            if len(word) > 3:
                if word[:3] not in prefix_counts:
                    prefix_counts[word[:3]] = 1
                else:
                    prefix_counts[word[:3]] += 1

    return prefix_counts


file_name = 'Text files/paper_soccer_functions_shuffled.py'
with open(file_name, 'r') as my_file:
    prefix_dict = prefix_counts(my_file)                                                                          

print(prefix_dict)


prefix_list = list(prefix_dict.keys())
random.shuffle(prefix_list)
most_common_prefix = prefix_list[0]
second_most_common_prefix = prefix_list[1]


for prefix in prefix_dict:
    if prefix_dict[prefix] > prefix_dict[most_common_prefix]:
        second_most_common_prefix = most_common_prefix
        most_common_prefix = prefix
    if prefix_dict[prefix] > prefix_dict[second_most_common_prefix]:
        second_most_common_prefix = prefix

print('The most common prefix is ' + most_common_prefix + ', occuring ' + str(prefix_dict[most_common_prefix]) + ' times')

print('The second most common prefix is ' + second_most_common_prefix + ', occuring ' + str(prefix_dict[second_most_common_prefix]) + ' times')
