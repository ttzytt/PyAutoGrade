



def letter_counts(read_file):
    letters = {}          
    for line in read_file:
        for char in line:
            if char in letters:
                letters[char] += 1
            else:
                letters[char] = 1
    return letters

def main():
    with open('Text files/greeneggs.txt', 'r') as input_file:
        data = letter_counts(input_file)
    for i in range(26):
        letter = chr(ord('A')+i) 
        
        upper = data[letter] if letter in data else 0
        lower = data[letter.lower()] if letter.lower() in data else 0
            
        print(letter, upper + lower )

if __name__ == '__main__':
    main()
