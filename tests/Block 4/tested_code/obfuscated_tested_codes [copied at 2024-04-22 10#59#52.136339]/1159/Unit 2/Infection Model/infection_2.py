


from infection_functions import *
import random
random.seed()

'''Set Up'''
board = original()
draw_board(board)
new_board = board
print()

'''Main Part'''
while 0 < count_patients(board) < 100:
    healing_rate = int(input('Input the healing rate(%): '))
    infection_rate = int(input('Input the infection rate(%): '))
    for row in range(10):
        for column in range(10):
            if check_neighbors(board,row,column) > 0 or board[row][column] == '+':
                if board[row][column] == '+':
                    get_cured = random.randint(1,100)
                    if get_cured <= healing_rate:
                        new_board[row][column] = ' '
                elif board[row][column] == ' ':
                    actual_infection_rate = infection_rate*check_neighbors(board,row,column)
                    get_infected = random.randint(1,100)
                    if get_infected <= actual_infection_rate:
                        new_board[row][column] = '+'
    board = new_board
    draw_board(board)
    print()
    print('Current patients: ' + str(count_patients(board)))
    print()
print('Simulation ended')



'''Set Up'''
from infection_functions import *
import random
random.seed()


board = original()
draw_board(board)
stop = '' 

print()
print('Current patients: 10')
print()


healing_rate = int(input('Input the healing rate(%): '))
infection_rate = int(input('Input the infection rate(%): '))

'''Main Part'''

while 0 < count_patients(board) < 100 and stop != 'stop':
    
    patients = []
    cured = []
    
    for row in range(10):
        
        for column in range(10):
            
            if board[row][column] == ' ': 
                neighbors = check_neighbors(board,row,column)
                actual_infection_rate = neighbors * infection_rate
                get_infected = random.randint(1,100)
                if get_infected <= actual_infection_rate: 
                    new_patient = [row,column]
                    patients.append(new_patient) 
                    
            elif board[row][column] == '+': 
                get_cured = random.randint(1,100)
                if get_cured <= healing_rate: 
                    new_cured = [row,column]
                    cured.append(new_cured) 
                else: 
                    new_patient = [row,column]
                    patients.append(new_patient) 

    board = draw_patients(board,patients,cured)
    draw_board(board)
    
    print()
    print('Current patients: ' + str(count_patients(board)))
    print()
    
    if 0 < count_patients(board) < 100:
        print('Press return/enter to continue, input \'stop\' to stop')
        stop = input()
    
print('Simulation ended')
