
populations = [(4,3)]

A  = 0.1
B = 0.2
C = 0.1
D = 0.02

deltaT = 0.12

nums = 500

K0 = 3
K1 = 1

for i in range(nums):
    new_rabbit_population = populations[i][0] + ((A * (K0 - populations[i][0])*populations[i][0])- B*populations[i][0]*populations[i][1])*deltaT
    new_sheep_population = populations[i][1] + ((C * (K1 - populations[i][1])*populations[i][1]) - D*populations[i][0]*populations[i][1])*deltaT
    populations.append((new_rabbit_population,new_sheep_population))
modified = []
for i in range(nums): 
    modified.append((populations[i][0], populations[i][1]))
print(modified)








