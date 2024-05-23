


import random
random.seed()







def house_lookup_v3(in_file): 
    house = ''
    words = {} 
    file = ((in_file.read()).split())
    i = 0
    while i < (len(file)-5):
        if file[i] == 'Albemarle':
            house = 'Albemarle'
            i +=1
        if file[i] == 'Ettl':
            house = 'Ettl'
            i +=1
        if file[i] == 'Hobler':
            house = 'Hobler'
            i +=1
        if file[i] == 'Lambert':
            house = 'Lambert'
            i +=1

        
        if file[i] != house:
            if ((('(') in file[i]) and (')') in file[i]) and file[i][1:-1] not in list(words.keys()):
                words[file[i][1:-1]] = [(file[i+1], house)] 
                i += 2 
            elif ((('(') in file[i]) and (')') in file[i]) and file[i][1:-1] in list(words.keys()):
                words[file[i][1:-1]].append((file[i+1], house))
                i += 2 
            
            
            elif (file[i] not in list(words.keys())) and (('(' and ')') not in file[i+1]):
                words[file[i]] = [(file[i+1], house)]
                i += 2
                
                
            elif (file[i] not in list(words.keys())) and (('(' and ')') in file[i+1]):
                words[file[i]] = [(file[i+2], house)]
                i += 1 
                
            elif file[i] in list(words.keys()):
                (words[file[i]]).append((file[i+1], house))
                i += 2 
    return(words)





def main():
    with open('Text file/houses, full.txt', 'r') as in_file:
        next_words = house_lookup_v3(in_file)

        
        while True:
            j = 0
            input_1 = input(('Input student name, in the format of Tom: '))
            if input_1 in list(next_words.keys()):
                if len(next_words[input_1]) == 1:
                    print('This student is in' , next_words[input_1][0][1])
                elif len(next_words[input_1]) > 1:
                    name = input_1
                    print('Did you mean ...')
                    while j < len(next_words[input_1]):
                        print(str(j+1) + '. ' + name + ' ' + next_words[input_1][j][0])
                        j += 1
                    sel = input("Enter the number for the student you want to know about:")
                    print('This student is in' , next_words[input_1][j-1][1])
                        
            if input_1 == 'quit': break 
            if input_1 not in list(next_words.keys()): print('Who dat?')
        
        
if __name__ == "__main__":
    main()

