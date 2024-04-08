








def romeo_and_juliet():
    Romeo = Starting_Romeo 
    Juliet = Starting_Juliet

    for i in range(1,51): 
        print(f'Day {i}:') 
        
        Romeo_new = Romeo + 0.4 * Juliet  
        Juliet_new = Juliet - 0.2 * Romeo

        Romeo = Romeo_new 
        Juliet = Juliet_new

        
        print(f"Romeo's love: {Romeo:.4f}") 
        print(f"Juliet's love: {Juliet:.4f}")
        if i != 50: 
            print()
            input('Press Enter to continue') 
            print()

        else: 
            print('Simulation over')
            
         
def neutral_romeo_and_juliet():
    Romeo = Starting_Romeo 
    Juliet = Starting_Juliet

    for i in range(1,51): 
        print(f'Day {i}:') 
        
        Romeo_new = 0.9 * Romeo + 0.4 * Juliet  
        Juliet_new = Juliet - 0.2 * Romeo

        Romeo = Romeo_new 
        Juliet = Juliet_new

        print(f"{Romeo:.4f}, {Juliet:.4f}")
        
        print(f"Romeo's love: {Romeo:.4f}") 
        print(f"Juliet's love: {Juliet:.4f}")
        
        if i != 50: 
            print()
            input('Press Enter to continue') 
            print()
            
        else: 
            print()
            print('Simulation over')


Starting_Romeo = int(input('Choose a starting love amount for Romeo: '))
Starting_Juliet = int(input('Choose a starting love amount for Juliet: '))




end_sims = False

while end_sims == False:
    print()
    
    chosen_sim = (input('Press 1 for the original simulation and press 2 for a modified '
          'simulation where romeo gets a little more neutral each day: '))

    if chosen_sim == '1':
        print()
        romeo_and_juliet()
        
    elif chosen_sim == '2':
        print()
        neutral_romeo_and_juliet()
        
    else: 
        print() 
        print('Invalid input. Please choose one or two')





