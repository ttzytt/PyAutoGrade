







def letter_counts(read_file):
    letter_diction = {} 
    words = (read_file.read()).split() 
    for i in range (len(words)):
        
        for j in range(len(words[i])): 
            if (words[i][j]) not in letter_diction.keys():
                letter_diction[words[i][j]] = 1 
            else:
                letter_diction[words[i][j]] += 1 
    return(letter_diction)








def main():
    with open('Text files/greeneggs.txt', 'r') as read_file:
        letter_diction = letter_counts(read_file)
        

        alpha = []
        letter = 'A'
        while letter <= 'Z':
            alpha.append(letter)
            letter = chr(ord(letter) + 1)
        
        for j in range (len(alpha)):
            print(alpha[j],end =" ")
            if (alpha[j] in letter_diction.keys()) and ((alpha[j].lower())
                                                        not in letter_diction.keys()):
                
                print (letter_diction[alpha[j]])
            elif (alpha[j] not in letter_diction.keys()) and ((alpha[j].lower())
                                                              in letter_diction.keys()):
                
                print (letter_diction[(alpha[j].lower())])
            elif (alpha[j] in letter_diction.keys()) and ((alpha[j].lower())
                                                          in letter_diction.keys()):
                print (letter_diction[alpha[j]]+letter_diction[(alpha[j].lower())])
                

            else:
                print(0) 

if __name__ == "__main__":
    main()
