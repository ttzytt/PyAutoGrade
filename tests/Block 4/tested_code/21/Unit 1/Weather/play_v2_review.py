




temperature = float(input('What is the temperature today(in °F)? '))



if temperature < 32 or temperature > 95:
        print('You shouldn’t play outside today.')
elif(temperature > 50):
 rain = str( input('Is it raining?(answer yes or no) ') )
 if rain == 'no':
        print('You should play outside today.')
 else:
  jacket = str( input ('Do you have a jacket?(answer yes or no) '))
  if(jacket == 'no'):
   print('You shouldn’t play outside today.') 
  else:
   print('You should play outside today.')
else:
  jacket = str( input ('Do you have a jacket?(answer yes or no) '))
  if(jacket == 'no'):
   print('You shouldn’t play outside today.') 
  else:
   print('You should play outside today.')


        
