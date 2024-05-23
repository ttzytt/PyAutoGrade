


import random
random.seed()





def house_lookup_v2(in_file): 
    house = ''
    words = {} 
    file = ((in_file.read()).split())
    
    i = 0
    while i < (len(file)-1):
        
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
            if file[i] not in list(words.keys()): 
                words[file[i]] = [(file[i+1], house)]
            elif file[i] in list(words.keys()): 
                (words[file[i]]).append((file[i+1], house))
            i += 2
    return(words)





def main():
    with open('Text file/houses, simplified.txt', 'r') as in_file:
        house_dictionary = house_lookup_v2(in_file)
        
        

        
        while True:
            j = 0
            input_1 = input(('Input student name, in the format of Tom: '))
            if input_1 in list(house_dictionary.keys()):
                if len(house_dictionary[input_1]) == 1: 
                    print('This student is in' , house_dictionary[input_1][0][1])
                    
                elif len(house_dictionary[input_1]) > 1:
                    name = input_1
                    print('Did you mean ...')
                    while j < len(house_dictionary[input_1]):
                        print(str(j+1) + '. ' + name + ' ' + house_dictionary[input_1][j][0])
                        j += 1
                    sel = int(input("Enter the number for the student you want to know about:"))
                    print('This student is in' , house_dictionary[input_1][sel-1][1])
                        
            if input_1 == 'quit': break 
            if input_1 not in list(house_dictionary.keys()): print('Who dat?')
        
        
if __name__ == "__main__":
    main()

