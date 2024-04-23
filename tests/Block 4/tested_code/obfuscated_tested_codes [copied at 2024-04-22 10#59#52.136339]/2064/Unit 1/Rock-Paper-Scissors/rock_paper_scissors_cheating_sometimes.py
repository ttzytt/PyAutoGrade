


import random

random.seed()

userChoice = input('Enter \'rock\' \'paper\' or \'scissors\': ')

cheatOrNotCheat = random.randint(1,10)



if(cheatOrNotCheat == 1):
    if (userChoice == 'rock'):                                 
        rps_choice = 'paper'
        print('I choose ' + rps_choice + ' I win!')
    elif (userChoice == 'paper'):                              
        rps_choice = 'scissors'
        print('I choose ' + rps_choice + ' I win!')
    elif (userChoice == 'scissors'):                           
        rps_choice = 'rock'
        print('I choose ' + rps_choice + ' I win!')
    else:
        print('''Wow, you suck.
⠀⢰⠲⢄⡀⠀⠀⠀⠀⠀⡏⠒⠤⡀⠀⠀⠀⠀⠀⠀
⠀⠘⡄⣀⠙⣦⠀⠀⣀⣰⡣⢸⠢⡈⠢⡀⠀⠀⠀⠀
⠀⠀⠸⡰⡰⠈⠉⠉⠀⠀⠀⠈⠑⠰⡀⠘⡄⠀⠀⠀
⠀⠀⢸⠏⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠸⡀⠀⠀
⠀⠀⡎⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢣⠀⠀
⢀⣾⡀⢳⢤⣀⠤⠀⠀⠀⢠⣀⣀⡀⠔⠀⠀⣸⠀⠀
⠘⢦⡀⡎⠀⡼⠁⠀⢻⠃⠀⠸⡄⠀⡅⠀⠈⢽⠀⠀
⠀⠀⠙⠤⣰⠃⠀⠀⠁⡖⠒⢼⡀⠐⣄⠤⠋⠁⠀⠀
⠀⠀⠀⠀⢀⡝⠒⡆⠀⠘⡄⠀⠻⣫⡀⠀⠀⠀⠀⠀
⠀⠀⠀⢠⠊⣀⡼⠀⠀⠀⠈⠢⢀⡠⠃⠀⠀⡰⠊⢱
⠀⠀⠀⠀⠉⠀⡇⠀⠀⠀⠀⠀⠀⡇⠀⡠⠊⣠⠔⠁
⠀⠀⠀⠀⠀⢸⠀⢤⠤⠤⠤⢤⠄⡯⠓⠋⠉⠀⠀⠀
⠀⠀⠀⠀⠀⠸⡠⠇⠀⠀⠀⠈⢆⠇⠀⠀⠀⠀⠀⠀
''')

else:
    num = random.randint(1,3)                                       
    if (num == 1):                                                  
        computer_rps_choice = 'rock'
    elif (num == 2):                                                
        computer_rps_choice = 'paper'
    elif (num == 3):
        computer_rps_choice = 'scissors'

    if (userChoice == 'rock' or userChoice == 'paper' or userChoice == 'scissors'):  
        if(userChoice == computer_rps_choice):              
            print('I played ' + computer_rps_choice + '! Draw!')
        elif((computer_rps_choice =='rock' and userChoice == 'scissors') or (computer_rps_choice =='scissors' and userChoice == 'paper') or (computer_rps_choice =='paper' and userChoice == 'rock')): 
            print('I played ' + computer_rps_choice + '! I win!') 
        else:                                               
            print('I played ' + computer_rps_choice + '! You win! Good game!')

    else:
        print('''You have angered the supreme all-mighty being of doom. Prepare to face the vengence of the mighty Meowthra!!
⠀⡤⠤⣀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣀⠠⢤⠀
⠀⠈⢧⡀⠉⠒⠤⣀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⠤⠒⠉⢀⣴⠃⠀
⠀⠀⠈⠻⡢⡀⠀⠀⡁⠢⠐⠒⠀⠉⠉⠉⠉⠁⠒⠒⠔⠊⠀⠀⢀⠔⠕⠁⠀⠀
⠀⠀⠀⠀⠈⢺⢆⢰⡟⠁⠀⠀⠀⣴⡴⢢⣦⠀⠀⠀⠀⠀⠀⠰⡧⠃⠀⠀⠀⠀
⠀⠀⠀⠀⠀⢸⠘⠋⠀⠀⠀⠀⠀⠁⠁⠀⠈⠀⠀⠀⠀⠀⠀⠀⡆⠀⠀⠀⠀⠀
⠀⠀⠀⠀⢀⠎⣀⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣀⠱⡀⠀⠀⠀⠀
⠀⠀⠀⠀⡜⢻⠍⠀⣀⡀⠀⠀⠀⠀⡀⢀⠀⠀⠀⠀⢀⣀⠀⠨⡿⢳⠀⠀⠀⠀
⠀⠀⠀⠀⢇⠀⠀⠀⠰⣌⠓⣲⠄⠀⠇⠘⡀⠠⣖⠘⣁⠜⠀⠀⠁⢸⠀⠀⠀⠀
⠀⠀⠀⠀⢸⠀⠀⠑⢄⡀⠀⢀⡠⠊⣀⣀⠑⢄⡀⠀⢀⡠⠚⠁⠀⡇⠀⠀⠀⠀
⠀⠀⠀⢀⠊⠀⠀⢀⡀⠬⡵⢧⠀⠈⣳⣟⠋⠀⡜⢾⠥⠀⣀⠀⠀⠘⡄⠀⠀⠀
⠀⠀⡰⠃⠀⠔⠊⠀⡤⠒⠹⣍⠐⠈⠓⠒⠉⢢⢉⠟⠒⢠⡀⠁⠢⠀⠈⢢⠀⠀
⠀⠜⠀⠀⠀⠀⢠⠋⠀⠀⠀⠀⠈⠉⠀⠂⠈⠁⠀⠀⠀⠀⠙⡄⠀⠀⠀⠀⠱⡀
⡜⠀⢠⡖⠤⢴⠆⠤⠄⠠⠠⠄⠠⠤⠀⠴⠠⠄⠤⠤⠤⠤⠦⠆⠀⠀⠤⠀⠀⠱
''')

