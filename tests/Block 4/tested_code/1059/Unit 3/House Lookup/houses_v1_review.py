


import random
random.seed()





def house_look_up(in_words): 
    house = ''
    House_dictionary = {} 
    words = ((in_words.read()).split())
    
    i = 0
    while i < (len(words)-1):
        
        if words[i] == 'Albemarle':
            house = 'Albemarle'
            i +=1
        if words[i] == 'Ettl':
            house = 'Ettl'
            i +=1
        if words[i] == 'Hobler':
            house = 'Hobler'
            i +=1
        if words[i] == 'Lambert':
            house = 'Lambert'
            i +=1

        
        if words[i] != house:
            House_dictionary[words[i] + ' ' + words[i+1][0]] = house
            i += 2
        
    return(House_dictionary)





def main():
    with open('Text file/houses, simplified.txt', 'r') as in_words:
        next_words = house_look_up(in_words)
        while True:
            input_1 = input(('Input student name, in the format of Tom Q: '))
            if input_1 in list(next_words.keys()):
                
                print('This student is in ' + next_words[input_1])
            if input_1 == 'quit': break
            
            if input_1 not in list(next_words.keys()): print('Who dat?')
            
                

if __name__ == "__main__":
    main()

