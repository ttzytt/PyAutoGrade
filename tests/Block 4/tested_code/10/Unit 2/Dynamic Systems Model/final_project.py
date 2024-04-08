








def rabbits_and_foxes_population(rabbits, foxes, rounds, num_trials):


        for i in range(num_trials):
                new_rabbits = rabbits + 0.01 * rabbits - 0.01 * rabbits * foxes
                new_foxes = foxes - 0.02 * foxes + 0.01 * rabbits * foxes
                
                
                round(new_rabbits, 4)
                round(new_foxes, 4)
                
                if foxes < 0:
                    foxes = 0
                if rabbits < 0:
                    rabbits = 0
                        
                if new_foxes < 0:
                    new_foxes = 0
                if new_rabbits < 0:
                    new_rabbits = 0
                    
                rabbits = new_rabbits
                foxes = new_foxes
                
                rounds += 1
                
                if rounds % 10 == 0:
                        list_of_points.append((new_rabbits, new_foxes))



               

while True:
        list_of_points = []
        rounds = 0
        new_rabbits = 0
        new_foxes = 0
        
        rabbits = float(input("how many rabbits?"))

        foxes = float(input("how many foxes?"))

        num_trials = int(input("how many days?"))
        
        rabbits_and_foxes_population(rabbits,foxes,rounds,num_trials)
        print(list_of_points)
