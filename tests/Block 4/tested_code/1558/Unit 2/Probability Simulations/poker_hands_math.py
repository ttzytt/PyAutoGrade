



"""
Simulation that calculates the odds of being dealt a full house
two of one rank and three of another
"""
def full_house_odds():
    
    total_ways = 1
    for i in range(5):
        total_ways *= 52 - i
        total_ways //= i + 1

    
    full_house_ways = (
        (13 * 4)  
        * (12 * 6)  
    )
    return (full_house_ways * 100) / total_ways


print(f"The odds of being dealt a full house are approximately: {full_house_odds()}%")


"""
Simulaition that calculates the odds of being dealt a straight flush, five in a
row, all the same suit. An ace can count as below a 2 or above a king but not
both.
"""
def straight_flush_odds():
 
    total_ways = 1
    for i in range(5):
        total_ways *= 52 - i
        total_ways //= i + 1

    
    straight_flush_ways = (
        
        (1 * 4)  
        +
        
        (9 * 4)  
        
        
        
    )
    return (straight_flush_ways * 100) / total_ways


print(f"The odds of being dealt a straight flush are approximately: {straight_flush_odds()}%")


"""
Simulation that calculates the odds of being dealt a flush, any five cards of the
same suit but not in a row
"""
def flush_odds():
    
    total_ways = 1
    for i in range(5):
        total_ways *= 52 - i
        total_ways //= i + 1

    
    flush_ways = (
        
        4  
        
        
        * (13 * 12 * 11 * 10 * 9) // (5 * 4 * 3 * 2 * 1)
    )

    return (flush_ways * 100) / total_ways


odds = flush_odds()
print(f"The odds of getting a flush are approximately {flush_odds()}%.")
