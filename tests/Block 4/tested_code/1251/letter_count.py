

def letter_counts(in_file):
    dcn = {}
    for text in in_file:
        for i in range(len(text)):
            
            if text[i] not in dcn:
                dcn[text[i]] = 1
            
            else:
                dcn[text[i]] += 1
    return dcn

def main():
    with open('Text files/words.txt', 'r') as in_file:
        dic = letter_counts(in_file)
        
        for i in range(65, 91):
            key = chr(i)
            if key in dic:
                
                if key.lower() in dic:
                    print(key + ' : ' + str(dic[key]+ dic[key.lower()]))
                
                else:
                    print(key + ' : ' + dic[key])
if __name__ == "__main__":
    main()
