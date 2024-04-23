











from infection_function import *

num_rows = int(input("Input how many rows u want: "))
num_columns = int(input("Input how many columns u want: "))

heal_probability = float(input('Input chance of healing as a decimal: '))
infection_probability = float(input('Input chance of infection as a decimal(keep value small): '))

num_infected_start = int(input('Input chance of people infected at start: '))

('''
# VACCINE toggle
vaccine_on = bool(input('Input wether you want vaccine mode on or off(true, false): '))

vaccine_discovery_chance = float(input('Input probablity of discovering a vaccine every 100 rounds(float): '))

# MUTATION toggle
mutation_on = bool(input('Input wether you want mutation mode on or off(true, false): '))

mutation_chance = float(input('Input probablity of a virus mutating every 100 rounds(float): '))
''')


num_infected = 0


round_number = 0

print('-------START SIMULATION-------')



board = []

create_grid(num_rows, num_columns, board)

place_infected(num_rows, num_columns, board, num_infected_start)




num_infected = count_infected(board, num_rows, num_columns)
print(num_infected)
print()


while(num_infected > 0 and (num_rows * num_columns - num_infected) > 0):
    print()
    print('start ROUND ' + str(round_number))

    
    
    
    board = execute_round(num_rows, num_columns, board, infection_probability, heal_probability)

    
    

    
    num_infected = count_infected(board, num_rows, num_columns)
    print(num_infected)
    print()
    
    

    
    round_number += 1
    
    ('''
    if vaccine_on:
        if round_number % 100 == 0:
            if random.random() < vaccine_discovery_chance:
                heal_probability += 0.07
    
    if mutation_on:
        if round_number % 100 == 0:
            if random.random() < mutation_chance:
                infection_probability += 0.085
    ''')

    
    if round_number >= 10000:
        print('OVER 10000, stopped code')
        break
