



temperature = float(input('What is the temperature today(in °F)? '))


if temperature < 32 or temperature > 95:
        print()
        print('You shouldn’t play outside today.')

        
elif temperature > 50: 
        rain = input('Is it raining?(answer yes or no) ')
        if rain == 'no':
                print()
                print('You should play outside today.')
        
        else: 
                jacket = input('Do you have a jacket?(answer yes or no) ')
                if jacket == 'no':
                        print()
                        print('You shouldn’t play outside today.')
                else:
                        print()
                        print('You should play outside today.')

                 

else:   
        jacket = input('Do you have a jacket?(answer yes or no) ')
        if jacket == 'no':
                print()
                print('You shouldn’t play outside today.')
        else:
                print()
                print('You should play outside today.')



        
