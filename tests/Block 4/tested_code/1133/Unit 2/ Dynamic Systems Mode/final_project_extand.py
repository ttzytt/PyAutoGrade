
def extended_model(point):
    rabbits, sheep = point
    delta_rabbits = 0.1 * (3 - rabbits) * rabbits - 0.2 * rabbits * sheep
    delta_sheep = 0.1 * (1 - sheep) * sheep - 0.02 * rabbits * sheep
    
    growth_rate_rabbits = delta_rabbits / rabbits if rabbits != 0 else 0
    growth_rate_sheep = delta_sheep / sheep if sheep != 0 else 0
    
    
    rate_of_change_rabbits = delta_rabbits
    rate_of_change_sheep = delta_sheep
    
    return {
        'new_rabbits': max(0, rabbits + delta_rabbits),
        'new_sheep': max(0, sheep + delta_sheep),
        'growth_rate_rabbits': growth_rate_rabbits,
        'growth_rate_sheep': growth_rate_sheep,
        'rate_of_change_rabbits': rate_of_change_rabbits,
        'rate_of_change_sheep': rate_of_change_sheep
    }
