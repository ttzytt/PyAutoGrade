

temperature = int(input('What is the temperature today (in °F)?')) 
robot = input('Are you a robot?')
if robot == 'Yes':
    print('Why do you need to know the weather?? Anyways...')
elif robot == 'No':
    print('Ok, cool. Solve this captcha.')
    answer = input('Are you a robot? ANSWER TRUTHFULLY.')
    if answer == 'No':
        print('LIES!')
    elif answer == 'Yes':
        print('Thanks for owning up to it.')
    
raining = input("Is it raining?")
if raining == 'Yes':
    jacket = input('Do you have a jacket?')
    if jacket == 'No':
        print("You shouldn't play outside today.")
        
    elif jacket == 'Yes' and temperature < 50 and temperature > 32:
        print('You should play outside today.')
        
    elif jacket == 'Yes' and temperature > 50 or temperature < 32:
        print("You shouldn't play outside today.")

elif raining == 'No' and temperature < 95 and temperature > 50:
    print('You should play outside today.')
    
elif raining == 'No' and temperature > 95 or temperature < 50:
    print ("You shouldn't play outside today.")
    








    

    
    
       
