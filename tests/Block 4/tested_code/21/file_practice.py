

file_name = 'Text files/words.txt'

result = []
for i in range(256):
    result.append(0)


with open(file_name,'r') as file:
    
    for line in file:
        X = line[:]
        
        for i in range(len(X)):
            
            result[ord(X[i])] += 1


for i in range(len(result)):
    
    if result[i] != 0 and i != 10:
        print(chr(i) +': '+ str(result[i]))
    
    if i == 10:
        print('line: ' + str(result[10]))
    
    
