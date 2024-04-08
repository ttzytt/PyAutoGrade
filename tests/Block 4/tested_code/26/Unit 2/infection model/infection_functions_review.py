


import random
random.seed()


def create_list(row,col):
    X = []
    for i in range(row+2):
        X.append([])
        for j in range(col+2):
            X[i].append(0)
    return X




def process(infection_probability,heal_probability,row,col,laststatus):
    matrix = create_list(row,col)

    for i in range(1,row+1):
        for j in range(1,col+1):
            
            if laststatus[i][j] == 1 and random.random() < heal_probability:
                 matrix[i][j] = 0
            
            
            
            
            elif laststatus[i][j] == 0 and random.random() < (1 - (1-infection_probability)**(laststatus[i+1][j]+laststatus[i-1][j]+laststatus[i][j+1]+laststatus[i][j-1])):
                matrix[i][j] = 1
    return matrix




def initialize(matrix, input_,row,col):
    x_ = 0
    y_ = 0
    for i in range(input_):
        while matrix[1+x_][1+y_]!= 0:
            x_ = random.randint(0,row-1)
            y_= random.randint(0,col-1)
        matrix[1+x_][1+y_] = 1


                  
