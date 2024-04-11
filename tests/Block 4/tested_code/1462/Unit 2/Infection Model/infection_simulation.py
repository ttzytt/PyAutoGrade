


import random
from infection_functions import *


heal_probability = float(input('Heal probability: '))
infection_probability = float(input('Infection probability: '))
repetition = int(input('Simulating times: '))




old_board = [ [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0],
            [0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0],
            [0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]]

draw_grid(old_board)
print('------------------')

infection_simulation(heal_probability, infection_probability, old_board, repetition)

"""
Questions I explored:
What combinations of probabilities lead to the virus eventually being eradicated,
and when does the virus stick around?

if I start with 5 infectants,
in order for it to be eradicated for each heal probability,
the infection probability should be...

 
Heal    Infection
0.1      < 0.01 (really small)
0.2      < 0.04 
0.3      < 0.06
0.4      < 0.09
0.5      < 0.15   
0.6      < 0.17
0.7      < 0.21
0.8      < 0.23
0.9      < 0.25
1.0      < 0.25

When there are approximately 5 infectants, the relationship between the
heal probability and infected probability is approximately linear.
"""


                
                
                
            
    
    
