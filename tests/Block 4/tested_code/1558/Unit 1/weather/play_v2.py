


"""
This program that lets the user input what the weather is
and prints out if the user should or should not play outside
"""


Farenheit = int(input('What is the temperature today ( In °F)? ' ))
Rain = (input('Is it raining? '))



if Rain == 'No' or 'no' and 50 < Farenheit < 95 :
    print ('You should play outside today')
elif Farenheit <= 32:
    print ('You should not play outside')
elif Farenheit >= 95:
    print ('You should play outside')

else:
    Jacket = (input('Do you have a jacket? '))
    
    
    
    if Jacket == 'Yes' or 'yes':
        print ('You should play outside ')
    else:
        print ('You should not play outside')
     


      
