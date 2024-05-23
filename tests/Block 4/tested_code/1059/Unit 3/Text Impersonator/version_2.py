


import random
random.seed()





def text_harvester(in_file): 
    fruit_loop = {} 
    current = ''
    for lines in in_file:
        text = lines.split()
        for i in range (len(text)):
            previous = current
            current = text[i]
            if (previous) not in fruit_loop.keys():
                fruit_loop[previous] = [current] 
            else:fruit_loop[previous].append(current) 

    fruit_loop.pop('')
    return(fruit_loop)


def text_impersonator(next_words, num_words, start_word = None):
    if start_word in (list(next_words.keys())):
        printing_list = [start_word]
    else:
        printing_list = []
        printing_list.append(random.choice(list(next_words.keys())))      
    
    for i in range(num_words-1):
        printing_list.append(random.choice(next_words[printing_list[-1]]))
    print(printing_list)
    return printing_list



def main():
    with open('Text files/greeneggs.txt', 'r') as in_file:
        next_words = text_harvester(in_file)
        num_words = 10
        start_word = 'success'
        text_impersonator(next_words, num_words, start_word)

if __name__ == "__main__":
    main()

