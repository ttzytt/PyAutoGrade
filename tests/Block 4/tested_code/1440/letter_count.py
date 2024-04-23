

import random

read_file = 'Text files/palindrom2.0.txt'


def letter_counts(read_file):
    alpha = {}
    for line in my_file:
        for j in line:
            if 64 < ord(j) < 90 or 97 < ord(j) < 122:
                if j not in alpha:
                    alpha[j] = 1
                else:
                    alpha[j] += 1
    print(alpha)
with (open(read_file,'r') as my_file): 
    letter_counts(read_file)
