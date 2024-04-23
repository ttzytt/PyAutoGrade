


def prefix_counts(read_file):

    prefix_dictionary = {}

    for line in read_file:

        words = line.split()

        for word in words:
            if len(word) >= 3:
                if word[ : 3] not in prefix_dictionary:
                    
