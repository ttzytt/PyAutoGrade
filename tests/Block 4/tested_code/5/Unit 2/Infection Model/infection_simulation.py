



from infection_functions import *
import random
random.seed()


healing_rate = 12
infection_rate = 40

patients = []
cured = []
board = [ [' ', ' ', ' ', ' ',' ',' ',' ',' ',' ',' '],
          [' ', ' ', ' ', ' ',' ',' ',' ',' ',' ',' '],
          [' ', ' ', ' ', ' ',' ',' ',' ',' ',' ',' '],
          [' ', ' ', ' ', ' ',' ',' ',' ',' ',' ',' '],
          [' ', ' ', ' ', ' ',' ',' ',' ',' ',' ',' '],
          [' ', ' ', ' ', ' ',' ',' ',' ',' ',' ',' '],
          [' ', ' ', ' ', ' ',' ',' ',' ',' ',' ',' '],
          [' ', ' ', ' ', ' ',' ',' ',' ',' ',' ',' '],
          [' ', ' ', ' ', ' ',' ',' ',' ',' ',' ',' '],
          [' ', ' ', ' ', ' ',' ',' ',' ',' ',' ',' ']]
while len(patients) < 20:
    row = random.randint(0,9)
    column = random.randint(0,9)
    patient = [row,column]
    if patient not in patients:
        board[row][column] = '+'
        patients.append(patient)
print('initial! ')
draw_board(board)
print()







while count_patients(board) > 0 and count_patients(board) < 100:
    print()
    patients = []
    cured = []
    for row in range(10):
        for column in range(10):
            if board[row][column] == ' ': 
                neighbors = check_neighbors(board,row,column)
                actual_infection_rate = neighbors*infection_rate
                get_infected = random.randint(1,100)
                if get_infected <= actual_infection_rate: 
                    new_patient = [row,column]
                    patients.append(new_patient)
                    
            elif board[row][column] == '+': 
                get_cured = random.randint(1,100)
                if get_cured <= healing_rate: 
                    new_cured = [row,column]
                    cured.append(new_cured)

    board = draw_patients_cured(board,patients,cured)
    draw_board(board)
    print()
    print('Current patients: '+str(count_patients(board)))
    print()
    attitude = input(('do you want to continue?'))
    if attitude == 'no':
        break
    print(board)
    
    
    
    
print('simulation ended')




