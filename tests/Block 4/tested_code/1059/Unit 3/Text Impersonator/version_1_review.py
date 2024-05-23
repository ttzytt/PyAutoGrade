


import random
random.seed()





def text_harvester(in_file): 
    word_dictionary = {} 
    file = ((in_file.read()).split())
    for i in range (len(file)-1): 
                                                    
        if (file[i]) not in word_dictionary.keys(): 
            word_dictionary[file[i]] = [file[i+1]] 
        else:word_dictionary[file[i]].append(file[i+1]) 
    return(word_dictionary)


def text_impersonator(next_words, num_words, start_word = None):
    signal = 0 
    if start_word in (list(next_words.keys())):
        printing_list = [start_word]
        
    elif (start_word is not None) and (start_word not in next_words):
        signal = 1 
        printing_list = [start_word]
        printing_list.append(random.choice(list(next_words.keys())))
        

        for i in range(num_words-2): 
            printing_list.append(random.choice(next_words[printing_list[-1]]))
    else:
        printing_list = [] 
        printing_list.append(random.choice(list(next_words.keys())))

    
    if signal == 0: 
        
        for i in range(num_words-1):
            printing_list.append(random.choice(next_words[printing_list[-1]]))
    
    
    
    return printing_list



def main():
    with open('Text for harvesting/William Shakespeare.txt', 'r') as in_file:
        next_words = text_harvester(in_file)
        num_words = 20
        start_word = 'prisms'
        list_print = text_impersonator(next_words, num_words, start_word)
        for i in range (len(list_print)):
            print(list_print[i],end =" ")

if __name__ == "__main__":
    main()

