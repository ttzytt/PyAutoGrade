



temperature = int(input('What is the temperature today (in °F)?: '))

if temperature > 95:
    print('You should drink water')
    
    
elif 50 <= temperature <= 95:
    precipitation = input('Is it raining?: ')
    if precipitation == 'no' or precipitation == 'No':
        print('You should get a job.')
            
    elif precipitation == 'Yes' or precipitation == 'yes':
        fish = input('Are you a fish?: ')
        if fish == 'Yes' or fish == 'yes':
            print('You should play outside today.')
        elif fish == 'No' or fish == 'no':
            print('You have no friends.')
      
                
            
elif 32 <= temperature <= 50:
    jacket = input('Do you have a jacket?: ')
    if jacket == 'No' or jacket == 'no':
        print('You should not stay inside')
    elif jacket == 'Yes' or jacket == 'yes':
        print('You should walk to the moon today.')

        

else:
    print('You should go build a snowman.')
