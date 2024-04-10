





with open('Text files/greeneggs.txt', 'r') as my_file:
    egg_count = 0
    for line in my_file: 
        words = line.split() 
        for word in words: 
            
            if word == "eggs":
                egg_count += 1

print('The story mentions the word eggs ' + str(egg_count) + ' times. ')






