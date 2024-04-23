



'''
Returns a dictionary. The keys are all the 3-letter prefixes and their corresponding
values are the number of times they occured.
inputs:
        read_file   A file open for reading
'''
def prefix_counts(read_file):

    prefix_to_number = {}

    for line in read_file:
        words = line.split()
        for word in words:
            if len(word) >= 3:
                word = word.lower()
                prefix = word[:3]
                if prefix in prefix_to_number:
                    prefix_to_number[prefix] += 1
                else:
                    prefix_to_number[prefix] = 1
                
    return prefix_to_number
        


file_name = 'Text files/t23_input.txt'
with open(file_name, 'r') as my_file:
    prefix_counted = prefix_counts(my_file)



most_common = {}
next_common = {}


most_common_times = 0
most_common_times = 0
for key in prefix_counted:
    if prefix_counted[key] > most_common_times:
        most_common = {key: prefix_counted[key]}
    elif prefix_counted == most_common_times:
        most_common[key] = prefix_counted[key]
    elif prefix_counted[key] > next_common_times:
        next_common = {key: prefix_counted[key]}
    elif prefix_counted == most_common_times:
        next_common[key] = prefix_counted[key]



