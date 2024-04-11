




from infection_functions import *
import random
random.seed()

healing_rate = 12
infection_rate = 40


patients = []
cured = []
rounds = 1

times = [[0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
               [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
               [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
               [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
               [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
               [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
               [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
               [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
               [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
               [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]]

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

while len(patients) < 10:
    row = random.randint(0,9)
    column = random.randint(0,9)
    patient = [row,column]
    if patient not in patients:
        board[row][column] = '+'
        times[row][column] += 1
        patients.append(patient)
print('First round begins!')
print('The infection board: ')
draw_board(board)
print('The times: ')
draw_board(times)
print()


while count_patients(board) > 0 and count_patients(board) < 100:
    rounds += 1
    print(str(rounds) + ' round begins!')
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
                    times[row][column] += 1
                    patients.append(new_patient)
                    
            elif board[row][column] == '+': 
                get_cured = random.randint(1,100)
                times[row][column] += 1
                if get_cured <= healing_rate: 
                    new_cured = [row,column]
                    cured.append(new_cured)

    board = draw_patients_cured(board,patients,cured)
    draw_board(board)
    print('Current patients: '+str(count_patients(board)))
    print()
    draw_board(times)
    attitude = input(('do you want to continue?'))
    if attitude == 'no':
        break
    

print('simulation ended')
probability_of_each_cells(times,rounds)
print('the infection probability of each cell is: ')
print(times)


