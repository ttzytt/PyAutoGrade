def letter_counts(read_file):
    fruit_loop = {}
    file = (read_file.read()).split()
    for i in range (len(file)):
        if len(file[i])>3:
            if (file[i][0:3]) not in fruit_loop.keys():
                fruit_loop[file[i][0:3]] = 1
            else:fruit_loop[file[i][0:3]] += 1
    print(fruit_loop)
    return(fruit_loop)






with open('Text files/T22_read.txt', 'r') as read_file:
    fruit_loop = letter_counts(read_file)
    temp_str1 = ''
    temp_int1 = 0
    temp_str2 = ''
    temp_int2 = 0
    for key in fruit_loop.keys():
        if fruit_loop[key] > temp_int1:
            temp_str2 = temp_str1
            temp_int2 = temp_int1
            temp_str1 = key
            temp_int1 = fruit_loop[key]
        if fruit_loop[key] > temp_int2 and key != temp_str1:
            temp_str2 = key
            temp_int2 = fruit_loop[key]
    print("The most common prefix is",temp_str1, "occurring",temp_int1, "times")
    print("The next most common prefix is",temp_str2, "occurring",temp_int2, "times")
