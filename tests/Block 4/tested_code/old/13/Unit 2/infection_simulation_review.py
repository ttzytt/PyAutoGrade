




from infection_functions import *
import random

def print_grid(grid):
    for row in grid:
        print(' '.join(row))
    print()

def run_simulation(size=10, infected_chance=0.1, heal_probability=0.3, infection_probability=0.2, rounds=50):
    
    grid = initialize_grid(size, infected_chance)
    print("Initial grid:")
    print_grid(grid)

    for round in range(rounds):
        grid = update_health_status(grid, heal_probability, infection_probability)
        print("Round " + str(round + 1) + ":")  
        print_grid(grid)

run_simulation(size=10, rounds=10)


def analyze_probabilities(size=10, rounds=100, trials=30):
    
    
    heal_probs = []
    infection_probs = []
    for i in range(1, 10):
        heal_probs.append(i / 10)
        infection_probs.append(i / 10)
    
    results = {}
    
    for heal_prob in heal_probs:
        for infection_prob in infection_probs:
            eradication_count = 0
            for i in range(trials):
                grid = initialize_grid(size, 0.1)  
                for j in range(rounds):
                    grid = update_health_status(grid, heal_prob, infection_prob)
                    if not any('x' in row for row in grid):
                        eradication_count += 1
                        break
            results[(heal_prob, infection_prob)] = eradication_count / trials

    return results


def format_results(results):
    heal_probs = []
    infection_probs = []

    
    for key in results.keys():
        if key[0] not in heal_probs:
            heal_probs.append(key[0])
        if key[1] not in infection_probs:
            infection_probs.append(key[1])

    heal_probs.sort()
    infection_probs.sort()

    
    print("Heal\\Infect", end='\t')
    for p in infection_probs:
        print(f"{p:.1f}", end='\t')
    print()  

    
    for heal_prob in heal_probs:
        print(f"{heal_prob:.1f}", end='\t')
        for infection_prob in infection_probs:
            eradication_likelihood = results.get((heal_prob, infection_prob), 0) * 100  
            print(f"{eradication_likelihood:.0f}%", end='\t')
        print()  




format_results(analyze_probabilities(10, 100, 30))

def infection_rate_by_location(size=10, heal_probability=0.5, infection_probability=0.5, rounds=100):
    
    grid = initialize_grid(size)
    
    location_status = {'corner': 0, 'edge': 0, 'center': 0}
    
    for i in range(rounds):
        grid = update_health_status(grid, heal_probability, infection_probability)
        for row in range(size):
            for col in range(size):
                location_type = 'center'
                if row in [0, size-1] and col in [0, size-1]:
                    location_type = 'corner'
                elif row in [0, size-1] or col in [0, size-1]:
                    location_type = 'edge'
                if grid[row][col] == 'x':
                    location_status[location_type] += 1

    for location in location_status:
        location_status[location] /= rounds
    return location_status

print(infection_rate_by_location(10, 0.5, 0.5, 100))

def update_health_status_with_immunity(grid, heal_probability, infection_probability, immunity_probability):
    
    new_grid = [row[:] for row in grid]
    for row in range(len(grid)):
        for col in range(len(grid[row])):
            if grid[row][col] == 'x' and random.random() < heal_probability:
                new_grid[row][col] = 'o' if random.random() < immunity_probability else '·'
            elif grid[row][col] == '·' and random.random() < infection_probability * count_infected_neighbors(grid, row, col):
                new_grid[row][col] = 'x'
            
    return new_grid

def run_simulation_with_immunity(size=10, infected_chance=0.1, heal_probability=0.3, infection_probability=0.2,immunity_probability=0.5, rounds=50):
    
    grid = initialize_grid(size, infected_chance)
    print("Initial grid:")
    print_grid(grid)

    for round in range(rounds):
        grid = update_health_status_with_immunity(grid, heal_probability, infection_probability,immunity_probability)
        print(f"Round {round+1}:")
        print_grid(grid)
        
run_simulation_with_immunity(size=10, rounds=10)
