



temperature = int(input('What is the temperature today (in °F)?: '))

if temperature > 95:
    print('You should not play outside today')
    
    
elif 50 <= temperature <= 95:
    precipitation = input('Is it raining?: ')
    if precipitation == 'no' or precipitation == 'No' :
        print('You should play outside today.')
            
    elif precipitation == 'Yes' or precipitation == 'yes':
        jacket = input('Do you have a jacket?: ')
        if jacket == 'No' or jacket == 'no':
            print('You should not play outside today.')
        elif jacket == 'Yes' or jacket == 'yes':
            print('You should play outside today')
                
            
elif 32 <= temperature <= 50:
    jacket = input('Do you have a jacket?: ')
    if jacket == 'No' or jacket == 'no':
        print('You should not play outside today')
    elif jacket == 'Yes' or jacket == 'yes':
        print('You should play outside today.')

        

elif temperature < 32:
    print('You should not play outside today.')



