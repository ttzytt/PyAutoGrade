



temperature_in_f = int(input('What is the temperature today (in °F)? '))


if((temperature_in_f > 95) or (temperature_in_f < 32)): 
    print('You shouldn\'t play outside today') #Says not to play outside
    
else:
    raining = input('Is it raining? ') #Checks if its raining
    if(raining == 'yes') or (raining == 'Yes'): #Confirms if it is raining
        jacket = input('Do you have a jacket? ') #If yes checks if it has jacket
        if(jacket == 'yes') or (jacket == 'Yes'): #Confirms there is jacket
            print('You should play outside today') #Tells user to play outside
        elif(jacket == 'no') or (jacket == 'No'): #Confirms there is no jacket
            print('You shouldn\'t play outside today') 
        else: 
            print('I\'m sorry we don\'t support this answer') 

    elif(raining == 'no') or (raining == 'No'): 
        print('You should play outside today') 

    else: 
        print('I\'m sorry we don\'t support this answer') 
            




