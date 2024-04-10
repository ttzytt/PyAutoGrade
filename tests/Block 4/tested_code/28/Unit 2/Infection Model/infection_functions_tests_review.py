


from infection_functions import *








def TEST(description, expected_result, actual_result):
    print(description, end = ': ')
    if actual_result == expected_result:
        print('pass')
    else:
        print('FAIL')
        print('   Expected result:', expected_result)
        print('   Actual result:', actual_result)

def get_magnitude(num):
    magnitude = 10
    while num // (1/10**(magnitude)) >= 1:
        magnitude -= 1
    return magnitude + 1

    

def RNG_TEST(description, expected_result, actual_result):
    print(description, ":")
    
    print("difference w/ magnitude ", get_magnitude(abs(expected_result-actual_result)))
    print('   Expected probability:', expected_result)
    print('   Actual probability:', actual_result)
    print()
    




def determine_if_infected_TEST(total_trials):

    infection_probabilities = [0.1,0,0.24,0.9,1,1]
    neighbors = [2,4,4,0,1,0]

    

    for i in range(len(neighbors)):
        infected = 0
        for _ in range(total_trials):
            if determine_if_infected(infection_probabilities[i], neighbors[i]):
                    infected += 1
        RNG_TEST(f"Infection Probability {infection_probabilities[i]} chance; {neighbors[i]} neighbors"
                 , infection_probabilities[i] * neighbors[i], infected/total_trials)

def determine_if_still_infected_TEST(total_trials):

    heal_probabilities = [0.63, 0.1, 0.9, 0, 1]

    

    for heal_probability in heal_probabilities:
        infected = 0
        healed = 0
        for _ in range(total_trials):
            if not determine_if_still_infected(heal_probability):
                healed += 1
        RNG_TEST(f"Heal Probability {heal_probability}", heal_probability, healed/total_trials)
            

def check_neighbors_TEST():
    TEST("4 neighbors", 4,
         check_neighbors([[False,True,False],[True,False,True],[False,True,False]],1,1))
    TEST("3 neighbors", 3,
         check_neighbors([[False,False,False],[True,False,True],[False,True,False]],1,1))
    TEST("2 neighbors", 2,
         check_neighbors([[False,True,False],[True,False,False],[False,False,False]],1,1))
    TEST("1 neighbor", 1,
         check_neighbors([[False,False,False],[True,False,False],[False,False,False]],1,1))
    TEST("0 neighbors", 0,
         check_neighbors([[False,False,False],[False,False,False],[False,False,False]],1,1))
    TEST("2 Neighbors Corner", 2,
         check_neighbors([[False,False,False],[False,False,True],[False,True,False]],2,2))
    TEST("3 Neighbors Edge", 3,
         check_neighbors([[True,False,True],[False,True,False],[False,False,False]],1,0))
    TEST("Full Board Infected Middle", 4,
         check_neighbors([[True,True,True],[True,True,True],[True,True,True]],1,1))
    TEST("1x1 Grid", 0,
         check_neighbors([[True]],0,0))

def is_everyone_healed_TEST():
    TEST("3x3 Everyone Infected", False,
        is_everyone_healed([[True,True,True],[True,True,True],[True,True,True]]))
    TEST("Random 1", False,
         is_everyone_healed([[True,False,True],[False,True,True],[True,True,False]]))
    TEST("Random 2", False,
         is_everyone_healed([[False,False,True],[False,True,False],[True,False,False]]))
    TEST("3x3 Everyone Healed", True,
         is_everyone_healed([[False,False,False],[False,False,False],[False,False,False]]))
    TEST("1x1 Everyone Healed", True,
         is_everyone_healed([[False]]))

def is_everyone_infected_TEST():
    TEST("3x3 Everyone Infected", True,
         is_everyone_infected([[True,True,True],[True,True,True],[True,True,True]]))
    TEST("Random 1", False,
         is_everyone_infected([[True,False,True],[False,True,True],[True,True,False]]))
    TEST("Random 2", False,
         is_everyone_infected([[False,False,True],[False,True,False],[True,False,False]]))
    TEST("3x3 Everyone Healed", False,
         is_everyone_infected([[False,False,False],[False,False,False],[False,False,False]]))
    TEST("1x1 Everyone Healed", False,
         is_everyone_infected([[False]]))
    TEST("1x1 Everyone Infected", True,
         is_everyone_infected([[True]]))



check_neighbors_TEST()
print("HIGHER MAGNITUDE = MORE ACCURATE")
determine_if_infected_TEST(10000)
determine_if_still_infected_TEST(10000)
is_everyone_healed_TEST()
is_everyone_infected_TEST()
