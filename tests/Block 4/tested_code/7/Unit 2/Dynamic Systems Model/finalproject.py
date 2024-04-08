




def no_competition_simulation(animals):
    
    new_rabbits = 0
    new_sheep = 0
    
    rabbits = animals[0]
    sheep = animals[1]

    
    
    if rabbits != 0:
        
        new_rabbits = rabbits + 0.1 * (3 - rabbits) * rabbits
    if sheep != 0:  
        new_sheep = sheep + 0.1 * (2 - sheep) * sheep

    
    if new_rabbits < 0:
        new_rabbits = 0
    if new_sheep < 0:
        new_sheep = 0
    return (new_rabbits, new_sheep)

def simulation_one(animals):
    
    new_rabbits = 0
    new_sheep = 0
    rabbits = animals[0]
    sheep = animals[1]
    if rabbits != 0:
        new_rabbits = rabbits + (0.1 * (3 - rabbits) * rabbits) - (0.2 * rabbits * sheep)
    if sheep != 0:  
        new_sheep = sheep + (0.1 * (2 - sheep) * sheep) - (0.1 * rabbits * sheep)

    if new_rabbits < 0:
        new_rabbits = 0
    if new_sheep < 0:
        new_sheep = 0
    return (new_rabbits, new_sheep)

def simulation_two(animals):
    
    new_rabbits = 0
    new_sheep = 0
    rabbits = animals[0]
    sheep = animals[1]
    if rabbits != 0:
        new_rabbits = rabbits + 0.1 * (3 - rabbits) * rabbits - 0.2 * rabbits * sheep
    if sheep != 0:  
        new_sheep = sheep + 0.1 * (1 - sheep) * sheep - 0.02 * rabbits * sheep

    if new_rabbits < 0:
        new_rabbits = 0
    if new_sheep < 0:
        new_sheep = 0
    return (new_rabbits, new_sheep)
rabbits = float(input('How many units of rabbits do you want to start with?'))
sheep = float(input('How many units sheep do you want to start with?'))
num_days = int(input('How many days is the simulation running for?'))
animals = (rabbits, sheep)
list_no_competition = [animals]
list_simulation_one = [animals]
list_simulation_two = [animals]
for _ in range(num_days-1):
    animals = no_competition_simulation(animals)
    list_no_competition.append(animals)

animals = (rabbits, sheep)
for _ in range(num_days-1):
    animals = simulation_one(animals)
    list_simulation_one.append(animals)

animals = (rabbits, sheep)
for _ in range(num_days-1):
    animals = simulation_two(animals)
    list_simulation_two.append(simulation_two(animals))

print(list_no_competition)
print()
print(list_simulation_one)
print()
print(list_simulation_two)
print()
