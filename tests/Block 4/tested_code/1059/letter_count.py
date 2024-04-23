def letter_counts(read_file):
    fruit_loop = {}
    file = (read_file.read()).split()
    for i in range (len(file)):
        for j in range(len(file[i])):
            if (file[i][j]) not in fruit_loop.keys():
                fruit_loop[file[i][j]] = 1
            else:fruit_loop[file[i][j]] += 1
    return(fruit_loop)






with open('Text files/T22_read.txt', 'r') as read_file:
    fruit_loop = letter_counts(read_file)
    alpha = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    for j in range (len(alpha)):
        print(alpha[j],end =" ")
        if (alpha[j] in fruit_loop.keys()) and ((alpha[j].lower()) not in fruit_loop.keys()):
            print (fruit_loop[alpha[j]])
        elif (alpha[j] not in fruit_loop.keys()) and ((alpha[j].lower()) in fruit_loop.keys()):
            print (fruit_loop[(alpha[j].lower())])
        elif (alpha[j] in fruit_loop.keys()) and ((alpha[j].lower()) in fruit_loop.keys()):
            print (fruit_loop[alpha[j]]+fruit_loop[(alpha[j].lower())])
        else:
            print(0)

