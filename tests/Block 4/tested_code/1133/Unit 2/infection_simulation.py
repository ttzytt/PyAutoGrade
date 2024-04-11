





from infection_functions import *
import random

def print_grid(grid):
    """Print the grid."""
    for row in grid:
        print(' '.join(row))
    print()

def run_simulation(size, infected_chance, heal_probability, infection_probability, rounds):
    """Run the infection simulation for a specified number of rounds."""
    num_rows, num_cols = size, size
    grid = initialize_grid(num_rows, num_cols, infected_chance)
    print("Initial grid:")
    print_grid(grid)

    for round in range(rounds):
        grid = update_health_status(grid, heal_probability, infection_probability)
        print("Round " + str(round + 1) + ":")
        print_grid(grid)

def analyze_probabilities(size, rounds, trials):
    """Analyze different combinations of heal and infection probabilities."""
    heal_probs = [i / 10 for i in range(1, 10)]
    infection_probs = [i / 10 for i in range(1, 10)]
    

    results = {}
    for heal_prob in heal_probs:
        for infection_prob in infection_probs:
            eradication_count = 0
            for _ in range(trials):
                grid = initialize_grid(size, size, 0.1)
                for _ in range(rounds):
                    grid = update_health_status(grid, heal_prob, infection_prob)
                    if not any('x' in row for row in grid):
                        eradication_count += 1
                        break
            results[(heal_prob, infection_prob)] = eradication_count / trials
    return results

def format_results(results):
    """Format and print the results of the simulation."""
    heal_probs = sorted(set(key[0] for key in results))
    infection_probs = sorted(set(key[1] for key in results))

    
    print("Heal/Infect")
    for p in infection_probs:
        print(round(p, 1), end=" ")
    print()  

    
    for heal_prob in heal_probs:
        print(round(heal_prob, 1))
        for infection_prob in infection_probs:
            eradication_likelihood = results.get((heal_prob, infection_prob), 0) * 100 
            
            
            print(round(eradication_likelihood, 0), "%", end=" ")
        print()  




run_simulation(size=10, infected_chance=0.1, heal_probability=0.3, infection_probability=0.2, rounds=10)
results = analyze_probabilities(size=10, rounds=100, trials=30)
format_results(results)
