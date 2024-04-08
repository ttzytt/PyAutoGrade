





num_trials = int(input('How many days do you want to simulate? '))
romeo = int(input('Input Romeo\'s initial value: '))
juliet = int(input('Input Juliet\'s initial value: '))

print('('+str(romeo)+','+str(juliet)+')', end = ', ') 

for count in range(num_trials):

    
    
    romeo_new = romeo + 0.4*juliet
    
    
    juliet_new = juliet - 0.2*romeo 

    romeo = romeo_new
    juliet = juliet_new
    

    if count < num_trials - 1:
        (print('(' + str(round(romeo_new*1000)/1000) + ','
               + str(round(juliet_new*1000)/1000) + ')', end = ', '))
    elif count == num_trials - 1:
        (print('(' + str(round(romeo_new*1000)/1000) + ','
               + str(round(juliet_new*1000)/1000) + ')', end = ' '))
    
   
