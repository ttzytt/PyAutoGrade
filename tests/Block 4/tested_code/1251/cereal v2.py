



dcn = {'red' : 6, 'blue' : 5, 'yellow': 7,'orange':7, 'purple':4,'green':6 }
input_ = 0
while input_ != 'quit':
    
    input_ = input('Enter any combinations of colors to find out the total number of fruit loops with those colors(type "quit" to quit): ')
    
    if input_ != 'quit':
        
        if 'floor' in input_:
            
            X = input_.split()
            for element in X:
                if element != ' ':
                    
                    if element in dcn:
                        dcn[element] += 1
                    
                    elif element != 'floor':
                        dcn[element] = 1
                    
        
        else:
            
            X = input_.split()
            result = 0
            for element in X:
                if element in dcn:
                    
                    result += dcn[element]
            
            print('There are ' + str(result) + ' fruit loops with those colors.')

