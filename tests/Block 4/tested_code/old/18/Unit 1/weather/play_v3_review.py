





temperature = int(input('What is the temperature today( In °F)? '))
if temperature >=100:
    print('That is so hot! I guess you will wait until the sun sets and then go play outside')

else:
    rain = (input('Is it raining? '))
    breathing = (input('Are you breathing? '))


    if breathing == 'No' and rain == 'Yes':
        print ('You WILL go outside and play, and since you are dead you do not even need a jacket.')
    elif breathing == 'No':
        print ('Since you are not breathing it would be unwise to play outside...'
           'But you WILL do it anyway')
    elif rain == 'No':
        print ('You WILL play outside today')

    else:
        
        jacket = (input('Do you have a jacket? '))
    
        if jacket == 'Yes':
            print ('Put on your jacket and you WILL play outside')
        else:
            
            money = (input('Do you have money? '))
            if money == 'Yes':
                print ('Go buy a jacket, put in on, and you WILL play outside')
            else:
                
                work = (input('Can you legally get a job? '))
                if work == 'Yes':
                    print ('Then go get a job, get paid, save up some money, buy a'
                               ' jacket, and you WILL play outside')
                else:
                    
                    time_machine = (input('Can you build a time machine? '))
                    if time_machine == 'Yes':
                        print ('Then travel to a time when you are a legal age to have a job,'
                                  ' get a job, get paid, save up some money, buy a jacket,'
                                    ' and you WILL play outside')
                    else:
                        print ('Then... go play video games inside.')
                        
